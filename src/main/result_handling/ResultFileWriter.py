import datetime


class ResultFileWriter(object):

    def write_analyzation_results_for_whole_corpus(comparison_results, output_path, textfile_name):
        now = datetime.datetime.now()

        text_file = open(output_path + textfile_name + "_" + now.strftime("%Y-%m-%d %H:%M"), "w")

        for result in comparison_results:
            ResultFileWriter.write_article_results_into_file(result,text_file)

        text_file.close()

    def write_article_results_into_file(comparison_result, file_to_write_to):
        file_to_write_to.write(comparison_result.get_result())

