import requests

from configuration import SERVICE_URL1
from src.baseclasses.response_test_two import Response_test_two
from src.schemas.user import User

resp = requests.get(url=SERVICE_URL1)


def test_getting_users_list():
    response = requests.get(url=SERVICE_URL1)
    test_object = Response_test_two(response)
    test_object.assert_status_code(300).validate(User)








#  {
#     'meta': {
#         'pagination': {
#             'total': 2919,
#             'pages': 292,
#             'page': 1,
#             'limit': 10,
#             'links': {
#                 'previous': None,
#                 'current': 'https://gorest.co.in/public/v1/users?page=1',
#                 'next': 'https://gorest.co.in/public/v1/users?page=2'
#             }
#         }
#     },
#     'data': [{
#         'id': 5685525,
#         'name': 'Bhishma Desai',
#         'email': 'bhishma_desai@goyette.test',
#         'gender': 'male',
#         'status': 'active'
#     }, {
#         'id': 5685523,
#         'name': 'Pushti Rana',
#         'email': 'rana_pushti@mckenzie-terry.test',
#         'gender': 'male',
#         'status': 'active'
#     }, {
#         'id': 5685521,
#         'name': 'Msgr. Ashlesh Marar',
#         'email': 'marar_msgr_ashlesh@hoeger.example',
#         'gender': 'male',
#         'status': 'active'
#     }, {
#         'id': 5685519,
#         'name': 'Dr. Daksha Nayar',
#         'email': 'daksha_dr_nayar@raynor-nicolas.example',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 5685518,
#         'name': 'Anjushri Khatri VM',
#         'email': 'anjushri_vm_khatri@weimann.test',
#         'gender': 'female',
#         'status': 'active'
#     }, {
#         'id': 5685517,
#         'name': 'Ekalavya Johar',
#         'email': 'ekalavya_johar@hoeger.test',
#         'gender': 'female',
#         'status': 'active'
#     }, {
#         'id': 5685516,
#         'name': 'Chanakya Deshpande',
#         'email': 'chanakya_deshpande@wuckert.test',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 5685514,
#         'name': 'Gov. Triloki Nath Varma',
#         'email': 'triloki_varma_gov_nath@casper-harber.test',
#         'gender': 'male',
#         'status': 'inactive'
#     }, {
#         'id': 5685513,
#         'name': 'Sharda Adiga',
#         'email': 'sharda_adiga@mcdermott-mohr.test',
#         'gender': 'female',
#         'status': 'inactive'
#     }, {
#         'id': 5685512,
#         'name': 'Brahmaanand Adiga',
#         'email': 'adiga_brahmaanand@kihn-bruen.test',
#         'gender': 'female',
#         'status': 'inactive'
#     }]
# }