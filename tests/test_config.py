# """tests the flask app configuration app.config.py"""
#
# import os
#
# from application import env_name
# from config import app_config
#
# # #
# # def test_development_config(test_app):
# # #     application.config.from_object(app_config[env_name])
# # #     assert application.config['SECRET_KEY'] == os.getenv('SECRET_KEY')
# #     assert test_app.config['TESTING']
#
#
# def test_testing_config(test_app):
#     test_app.config.from_object(app_config[env_name])
#     # assert test_app.config['SECRET_KEY'] == os.getenv('SECRET_KEY')
#     assert test_app.config['TESTING']
