# import pytest
# from model.initialization import Initialization
# from model.account import Account
# # Функция создающая фикстуру
# # requset.addfinalizer - параметр с методом разрушающий фикстуру
#
# # @pytest.fixture(scope = "session")
# # def app(request):
# #     fixture = Initialization()
# #     fixture.session.login(Account(username=" ", password=" "))
# #     def fin():
# #         fixture.session.logout()
# #         fixture.destroy()
# #     request.addfinalizer(fin)
# #     return fixture
#
#
# # Интелектуальная фикстура с проверкой валидности
# fixture = None
#
# @pytest.fixture
# def app(request):
#     global fixture
#     if fixture is None:
#         fixture = Initialization()
#         # fixture.session.login(Account(username=" ", password=" "))
#     else:
#         if not fixture.is_valid():
#             fixture = Initialization()
#             # fixture.session.login(Account(username=" ", password=" "))
#     fixture.session.ensure_login(Account(username=" ", password=" "))
#     return fixture
#
#
# # autouse=True - позволяет выполнятся stop автоматически без указания в каком либо методе
# # @pytest.fixture(scope="session", autouse=True)
# # def stop(request):
# #     def fin():
# #         fixture.session.logout()
# #         fixture.destroy()
# #     request.addfinalizer(fin)
# #     return fixture
#
#
# #Модуль: интелектуальный Login и Logout
# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     def fin():
#         fixture.session.ensure_logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture