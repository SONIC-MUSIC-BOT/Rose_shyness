from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ايقاف مؤقتاً",
            description=f"لايقاف تشغيل الموسيقى مؤقتاً في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="استئناف التشغيل",
            description=f"لاستئناف تشغيل الموسيقى المتوقفه مؤقتاً في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="تخطي الموسيقى",
            description=f"لتخطي الموسيقى المشتغله الى الموسيقى التي بعدها في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="انهاء التشغيل",
            description="لانهاء تشغيل الموسيقى في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="خلط القائمه",
            description="لخلط قائمة التشغيل في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="تكرار الموسيقى",
            description="لتكرار الموسيقى المشتغله 3 مرات في المجموعه.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
