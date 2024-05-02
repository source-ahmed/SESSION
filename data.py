from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("- ابـدا بأستخراج كـود .", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجوع", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("السورس", url="https://t.me/D2_RK")],
        [
            InlineKeyboardButton("- المساعده .", callback_data="help"),
            InlineKeyboardButton("- حول البوت .", callback_data="about")
        ],
        [InlineKeyboardButton("‹ المطور ›", url="https://t.me/A7_M3")],
    ]

    START = """
📟 ¦ أهلا بك عزيزي {} \n🖱 ¦ يمكنك استخراج التالي 📥\n📟 ¦ تيرمكس تيلثون للحسابات 🥷\n📡 ¦ تيرمكس تيلثون للبوتات 🎭\n🎸 ¦ بايروجرام ميوزك للحسابات 🥷\n🔮 ¦ بايروجرام ميوزك للبوتات 🎭\n🔗 ¦ بايروجرام ميوزك أحدث اصدار 📀\n\n- يعمل هـذا البوت لمساعدتـك بطريقـة سهله للحصول على كود تيرمكس لتشغيل تيلثون والبايروجرام لتشغيل سورس اغاني تم أنشاء هذا البوت\n\nبواسطـة : [احـمد الهكر](https://t.me/A7_M3) 
    """

    HELP = """
**↢ للحصول علي مساعده 🕹️** 

`/about` - معلومات البوت
`/generate` - بدأ الاستخراج
`/cancel` - الغاء الاستخراج
`/start` - لبدا البوت 
"""

    ABOUT = """
**↢ معلومات البوت الاستخراج 🔎** 

بوت لاستخراج سلسلة الجلسات Pyrogram و Telethon

Developer : [DaRk](https://t.me/A7_M3)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)
    """
  

