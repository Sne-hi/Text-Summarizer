# from textSummarizer.config.configuration import ConfigurationManager
# from textSummarizer.components.data_validation import DataValidation
# from textSummarizer.logging import logger


# class DataValidationTrainingPipeline:
#     def __init__(self):
#         pass

#     def main(self):
#         config = ConfigurationManager()
#         data_validation_config = config.get_data_validation_config()
#         data_validation = DataValidation(config=data_validation_config)
#         data_validation.download_data()
#         data_validation.unzip_and_clean_data()
        

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationPipeline:

    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        data_validation_config = self.config.get_data_validation_config()

        data_validation = DataValidation(
            config=data_validation_config
        )

        status = data_validation.validate_all_files_exist()

        return status