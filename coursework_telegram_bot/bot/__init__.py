import telebot
import os
from bot.handlers import handlerCourses,handlerCourse,handlerTests,handlerTest,handlerResultTests,handlerStart,handlerMessages
from dotenv import load_dotenv,find_dotenv



load_dotenv(find_dotenv())
bot=telebot.TeleBot(os.getenv('token'))

handlerStart.start(bot)
handlerCourses.courses(bot)
handlerCourse.course(bot)
handlerTests.tests(bot)
handlerTest.test(bot)
handlerResultTests.resultTest(bot)
handlerMessages.messages(bot)


