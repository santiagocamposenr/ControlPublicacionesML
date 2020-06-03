from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
#import logging
#logging.basicConfig(level=logging.INFO)
from scraper import Scraper_juguetimax
from get_product_links import get_links
from get_current_status import get_current_status

#logger = logging.getLogger(__name__)

def check_status():
    #logger.info('initiating status check')
    print('initiating status check')
    rows_changed = {}
    rows_bad_links = {}

    spreadsheet_id = "1j0GvVT41xTc-mMLuyar2SEE7A3b8B8q4eItXdUhryz0"
    range_for_links = 'Todas!C:C'
    range_for_status = 'Todas!E:E'

    row_link = get_links(spreadsheet_id, range_for_links)
    row_status = get_current_status(spreadsheet_id, range_for_status)
    
    scraper = Scraper_juguetimax()
    for row, link in row_link.items():
        if link == []:
            continue
        else:
            scraper.search_product(link)
            availability = scraper.get_availability()
            if availability == 'entrega inmediata':
                new_status = 'activa'
            else:
                if availability == None:
                    print('availability not found for link in row', row)
                    print('availability not found for link:\n', link)
                    request_status = scraper.check_request_status(link)
                    print('request status =', request_status)
                    new_status = 'pausada'
                    #aqui registro los link donde no se encontro availability
                    #en las tuplas se registra el link el estatus de la request
                    rows_bad_links[row] = (link, request_status)
                else:
                    new_status = 'pausada'

            if new_status == row_status[row]:
                pass
            else:
                #aqui registro las filas donde cambio es status 
                #en las tuplas el primer elemento es el status de la sheet y el segundo es el status de la pagina de juguetimax
                rows_changed[row] = (row_status[row], new_status)

    scraper.log_out()
    scraper.close_driver()
    
    return rows_changed, rows_bad_links
  
if __name__ == '__main__':
    rows_changed, rows_bad_links = check_status()
    print(rows_changed)
    print(rows_bad_links)