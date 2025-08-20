import sentry_sdk

sentry_sdk.init(
    dsn="https://dd9a0e91e9c159ecb8e42063b8407b6c@o4509877806759936.ingest.us.sentry.io/4509877815017472",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

division_by_zero = 1 / 0