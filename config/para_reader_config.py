### lambda machine
class READER_CONFIG(object):
    """docstring for CONFIG"""
    def __init__(self):
        super(READER_CONFIG, self).__init__()

        '''
        In the turing machine, all of my data are storing in: /tank/space/chen_zheng/data/hotpotqa/rangers/data/
        Data description:
        dev_selected_paras.json  
        train_selected_paras.json :  result generateed from select_paragraph model (retrieval)
        hotpot_dev_distractor_v1.json  
        hotpot_train_v1.1.json : raw data from hotpot webpage
        hotpot_dev_squad.json  
        hotpot_train_squad.json  : the result generated from my code, which combines selected_paras.json and raw data(raw data with only 2-3 paragraphs) 
                                    and transfer to squad format, then the model can learn by (reader) model

        Note that in the reader training section, we need to do the feature from squad data, and we store to the same folder of squad file.
        like: cached_train_features_file = reader_cfg.train_file + '_{0}_{1}_{2}_{3}
        '''

        self.visable_gpus = 4,
        # self.bert_model = 'bert-base-uncased' ## bert-base-uncased, bert-large-uncased, bert-base-cased, bert-base-multilingual, bert-base-chinese. roberta-base, roberta-large.
        # self.bert_model = 'bert-large-uncased-whole-word-masking'
        # self.bert_model = 'roberta-base'
        self.bert_model = 'albert-large-v2'  ###### albert-base-v2, albert-large-v2, albert-xlarge-v2, albert-xxlarge-v2
        self.do_lower_case = True          ## Set this flag if you are using an uncased model. Whether to lower case the input text. True for uncased models, False for cased models.

        # self.output_dir = '/home/hlr/shared/data/chenzheng/data/hotpotqa/models/hotpot_models/reader_4_2_change_is_impossible/'                  ## The output directory where the model checkpoints and predictions will be written.
        
        # self.output_dir = '/home/hlr/shared/data/chenzheng/data/hotpotqa/models/hotpot_models/reader_4_28_robert_bert/'                  ## The output directory where the model checkpoints and predictions will be written.
        # self.train_file = '/home/hlr/shared/data/chenzheng/data/hotpotqa/rangers/data/hotpot_train_squad.json'                  ## SQuAD-format json file for training.
        # self.predict_file = '/home/hlr/shared/data/chenzheng/data/hotpotqa/rangers/data/hotpot_dev_squad.json'                ## SQuAD-format json file for evaluation.


        # self.output_dir = '/tank/space/chen_zheng/data/hotpotqa/rangers/models/reader_4_29_robert_based_only_train_3_epoches/'                  ## The output directory where the model checkpoints and predictions will be written.
        self.output_dir = '/tank/space/chen_zheng/data/hotpotqa/rangers/models/reader_5_1_albert_large_only_train_3_epoches/'                  ## The output directory where the model checkpoints and predictions will be written.
        self.train_file = '/tank/space/chen_zheng/data/hotpotqa/rangers/data/hotpot_train_squad.json'                  ## SQuAD-format json file for training.
        self.predict_file = '/tank/space/chen_zheng/data/hotpotqa/rangers/data/hotpot_dev_squad.json'                ## SQuAD-format json file for evaluation.
        self.max_seq_length = 384             ## The maximum total input sequence length after WordPiece tokenization. Sequences "
                                            ## "longer than this will be truncated, and sequences shorter than this will be padded."
        self.doc_stride = 128               ## When splitting up a long document into chunks, how much stride to take between chunks.
        self.max_query_length = 64          ## The maximum number of tokens for the question. Questions longer than this will be truncated to this length.
        self.do_train = True                ## Whether to run training.
        self.do_predict = True             ## Whether to run eval on the dev set.
        # self.train_batch_size = 32           ## Total batch size for training.
        self.train_batch_size = 4           ## Total batch size for training.
        self.predict_batch_size = 4         ## Total batch size for predictions.
        self.learning_rate = 5e-5
        self.num_train_epochs = 3.0         ## float
        self.warmup_proportion = 0.1        ## Proportion of training to perform linear learning rate warmup for. E.g., 0.1 = 10%% of training.
        self.n_best_size = 20               ## The total number of n-best predictions to generate in the nbest_predictions.json output file.
        self.max_answer_length = 30         ## The maximum length of an answer that can be generated. This is needed because the start and end predictions are not conditioned on one another.
        self.verbose_logging = True         ## If true, all of the warnings related to data processing will be printed.
                                            ## A number of warnings are expected for a normal SQuAD evaluation.
        self.no_cuda = False                ## Whether not to use CUDA when available
        self.seed = 42                      ## random seed for initialization
        self.gradient_accumulation_steps = 1 ## Number of updates steps to accumulate before performing a backward/update pass.
        self.local_rank = -1                ## local_rank for distributed training on gpus
        self.fp16 = False                   ##  Whether to use 16-bit float precision instead of 32-bit
        self.loss_scale = 0                 ## Loss scaling to improve fp16 numeric stability. Only used when fp16 set to True.\n"
                                            ## "0 (default value): dynamic loss scaling.\n"
                                            ## "Positive power of 2: static loss scaling value.\n"
        # self.version_2_with_negative = False ## If true, the SQuAD examples contain some that do not have an answer.
        self.version_2_with_negative = True ## If true, the SQuAD examples contain some that do not have an answer.
        self.null_score_diff_threshold = 0.0 ## If null_score - best_non_null is greater than the threshold predict null.
        self.server_ip = ''                 ## Can be used for distant debugging.
        self.server_port = ''               ## Can be used for distant debugging.
        self.no_masking = False             ## If true, we do not mask the span loss for no-answer examples.
        self.skip_negatives = False         ## If true, we skip negative examples during training; this is mainly for ablation.
        self.max_answer_len = 1000000       ## maximum length of answer tokens (might be set to 5 for Natural Questions!)
        self.lambda_scale = 1.0             ## If you would like to change the two losses, please change the lambda scale.
        self.save_gran = None               ## "10,5" means saving a checkpoint every 1/10 of the total updates, but start saving from the 5th attempt





##### turing machine
# class READER_CONFIG(object):
#     """docstring for CONFIG"""
#     def __init__(self):
#         super(READER_CONFIG, self).__init__()

#         '''
#         In the turing machine, all of my data are storing in: /tank/space/chen_zheng/data/hotpotqa/rangers/data/
#         Data description:
#         dev_selected_paras.json  
#         train_selected_paras.json :  result generateed from select_paragraph model (retrieval)
#         hotpot_dev_distractor_v1.json  
#         hotpot_train_v1.1.json : raw data from hotpot webpage
#         hotpot_dev_squad.json  
#         hotpot_train_squad.json  : the result generated from my code, which combines selected_paras.json and raw data(raw data with only 2-3 paragraphs) 
#                                     and transfer to squad format, then the model can learn by (reader) model

#         Note that in the reader training section, we need to do the feature from squad data, and we store to the same folder of squad file.
#         like: cached_train_features_file = reader_cfg.train_file + '_{0}_{1}_{2}_{3}
#         '''

#         self.visable_gpus = 1,2,3,5
#         self.bert_model = 'bert-base-uncased' ## bert-base-uncased, bert-large-uncased, bert-base-cased, bert-base-multilingual, bert-base-chinese.
#         # self.bert_model = 'bert-large-uncased-whole-word-masking'
#         self.do_lower_case = True          ## Set this flag if you are using an uncased model. Whether to lower case the input text. True for uncased models, False for cased models.

#         self.output_dir = '/tank/space/chen_zheng/data/hotpotqa/models/hotpot_models/reader_4_2_change_is_impossible/'                  ## The output directory where the model checkpoints and predictions will be written.
#         self.train_file = '/tank/space/chen_zheng/data/hotpotqa/rangers/data/hotpot_train_squad.json'                  ## SQuAD-format json file for training.
#         self.predict_file = '/tank/space/chen_zheng/data/hotpotqa/rangers/data/hotpot_dev_squad.json'                ## SQuAD-format json file for evaluation.
#         self.max_seq_length = 384             ## The maximum total input sequence length after WordPiece tokenization. Sequences "
#                                             ## "longer than this will be truncated, and sequences shorter than this will be padded."
#         self.doc_stride = 128               ## When splitting up a long document into chunks, how much stride to take between chunks.
#         self.max_query_length = 64          ## The maximum number of tokens for the question. Questions longer than this will be truncated to this length.
#         self.do_train = True                ## Whether to run training.
#         self.do_predict = True             ## Whether to run eval on the dev set.
#         self.train_batch_size = 32           ## Total batch size for training.
#         self.predict_batch_size = 8         ## Total batch size for predictions.
#         self.learning_rate = 5e-5
#         self.num_train_epochs = 3.0         ## float
#         self.warmup_proportion = 0.1        ## Proportion of training to perform linear learning rate warmup for. E.g., 0.1 = 10%% of training.
#         self.n_best_size = 20               ## The total number of n-best predictions to generate in the nbest_predictions.json output file.
#         self.max_answer_length = 30         ## The maximum length of an answer that can be generated. This is needed because the start and end predictions are not conditioned on one another.
#         self.verbose_logging = True         ## If true, all of the warnings related to data processing will be printed.
#                                             ## A number of warnings are expected for a normal SQuAD evaluation.
#         self.no_cuda = False                ## Whether not to use CUDA when available
#         self.seed = 42                      ## random seed for initialization
#         self.gradient_accumulation_steps = 1 ## Number of updates steps to accumulate before performing a backward/update pass.
#         self.local_rank = -1                ## local_rank for distributed training on gpus
#         self.fp16 = False                   ##  Whether to use 16-bit float precision instead of 32-bit
#         self.loss_scale = 0                 ## Loss scaling to improve fp16 numeric stability. Only used when fp16 set to True.\n"
#                                             ## "0 (default value): dynamic loss scaling.\n"
#                                             ## "Positive power of 2: static loss scaling value.\n"
#         # self.version_2_with_negative = False ## If true, the SQuAD examples contain some that do not have an answer.
#         self.version_2_with_negative = True ## If true, the SQuAD examples contain some that do not have an answer.
#         self.null_score_diff_threshold = 0.0 ## If null_score - best_non_null is greater than the threshold predict null.
#         self.server_ip = ''                 ## Can be used for distant debugging.
#         self.server_port = ''               ## Can be used for distant debugging.
#         self.no_masking = False             ## If true, we do not mask the span loss for no-answer examples.
#         self.skip_negatives = False         ## If true, we skip negative examples during training; this is mainly for ablation.
#         self.max_answer_len = 1000000       ## maximum length of answer tokens (might be set to 5 for Natural Questions!)
#         self.lambda_scale = 1.0             ## If you would like to change the two losses, please change the lambda scale.
#         self.save_gran = None               ## "10,5" means saving a checkpoint every 1/10 of the total updates, but start saving from the 5th attempt