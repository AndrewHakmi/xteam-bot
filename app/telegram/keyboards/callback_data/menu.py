from aiogram.filters.callback_data import CallbackData


class CDAbout(CallbackData, prefix="about"):
    pass


class CDMenu(CallbackData, prefix="menu"):
    pass
