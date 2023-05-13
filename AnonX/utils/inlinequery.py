from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ايقاف مؤقتاً",
            description=f"لايقاف تشغيل الموسيقى مؤقتاً في المجموعه.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="استئناف التشغيل",
            description=f"لاستئناف تشغيل الموسيقى المتوقفه مؤقتاً في المجموعه.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="تخطي الموسيقى",
            description=f"لتخطي الموسيقى المشتغله الى الموسيقى التي بعدها في المجموعه.",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="انهاء التشغيل",
            description="لانهاء تشغيل الموسيقى في المجموعه.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="خلط القائمه",
            description="لخلط قائمة التشغيل في المجموعه.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="تكرار الموسيقى",
            description="لتكرار الموسيقى المشتغله 3 مرات في المجموعه.",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
