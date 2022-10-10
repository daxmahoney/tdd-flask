class BaseConfig:
    Testing = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingCOnfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
