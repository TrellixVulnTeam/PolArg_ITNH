class TokenCounter:

    @staticmethod
    def count_article_tokens(self, article_to_count):
        # only needed if article_to_count is a string
        token_list = article_to_count.split(' ')
        token_count = len(token_list)

        return token_count

    def count_average_sentence_length(self, article_to_count):
        # only needed if article_to_count is a string
        sentence_list = article_to_count.split('. ')
        # counts the number of sentences
        number_of_sentences = len(sentence_list)
        # adds the sentence lengths
        word_counter = 0
        for sentence in sentence_list:
            word_list = ' '.join(self, sentence)
            sentence_length = len(word_list)
            word_counter += sentence_length

        average_sentence_length = word_counter / number_of_sentences

        return average_sentence_length

    def count_number_of_sub_sentences(self, article_to_count):
        token_list = ' '.join(self, article_to_count)
        token_list = token_list.split(',')
        sub_sentence_list = []
        for sentence in token_list:
            if '. ' in sentence:
                continue;
            else:
                if len(sentence) > 25:
                    sub_sentence_list.append(sentence)
        return len(sub_sentence_list)





