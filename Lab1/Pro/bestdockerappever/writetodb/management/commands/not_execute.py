import random

from django.core.management.base import BaseCommand, CommandError

from writetodb.models import BootRecord


class Command(BaseCommand):

    def handle(self, *args, **options):
        random_paste_array = [[
            "Ну и зачем ты это сделал? Кто тебя просил? "
            "Мне очень жаль что ты не следуешь простейшим указаниям в навазнии файлов. "
            "На дворе уже ", " ,а ты никак не научишься. Еще и автоматизировал запуск. Кошмар"],
            ["ДАМЫ И ГОСПОДА, ЛЕДИ И ДЖЕНТЕЛЬМЕНЫ, А ТАКЖЕ ВСЕ ИНТЕРЕСУЮЩИЕСЯ! СЕГОДНЯ ",
             " Я ПРЕДСТАВЛЯЮ ВАШЕМУ ВНИМАНИЮ ИСПОЛЬЗОВАНИЕ КОМПОУЗА, ДЖАНГИ И ПОСТГРЕСА"],
            ["Дата: ", " я совершил чудовщиную ошибку. я выполнил тот скрипт который выполнять "
                       "было нельзя. назад дороги нет."]]
        br = BootRecord.objects.create()
        random_paste = random.choice(random_paste_array)
        br.copy_paste =  random_paste[0] + str(br.date_add)+random_paste[1]
        br.save()
        print("done")
