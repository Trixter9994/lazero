import abc
from nalaf.structures.data import Relation
from nalaf.features import get_spacy_nlp_english
from nalaf.preprocessing.spliters import GenericSplitter, NLTK_SPLITTER
from nalaf.preprocessing.tokenizers import GenericTokenizer, NLTK_TOKENIZER
from nalaf.preprocessing.edges import SentenceDistanceEdgeGenerator


class Annotator(object):
    """
    Abstract class for Entity tagging or Relationship tagging.
    This forms a hierarchy, where Tagger and RelationExtractor are abstract
    subclasses of Annotator
    """

    def __init__(self, predicts_classes):
        self.predicts_classes = predicts_classes
        """a list of class IDs that this tagger can predict"""


    @abc.abstractmethod
    def annotate(self, dataset):
        """
        In general, do and add predictions to the dataset, i.e., annotate the dataset

        :type dataset: nalaf.structures.data.Dataset
        """
        pass


class Tagger(Annotator):
    """
    Abstract class for (entity-) tagging a dataset with predicted annotations.

    Subclasses that inherit this class should:
    * Be named [Name]Tagger
    * Implement the abstract method tag
    * Use some sort of model or service to generate predictions
        * If you only want to read in predictions already saved in ann.json
         use AnnJsonAnnotationReader with _is_predicted = True
    * Append new items to the list field "predicted_annotations" of each Part in the dataset
    * Set the meta_attribute predicts_classes

    Optionally the implementation may perform normalization of the predicted entities.
    In that case:
    * set the meta attribute does_normalization = True
    * set the meta attribute normalization_database
    * set the fields normalized_id and normalized text for each Annotation object you create

    :type does_normalization: bool
    :type normalization_database: str
    :type predicts_classes: list[str]
    """

    # todo change normalizazion_database to normalise option
    def __init__(self, predicts_classes):
        super().__init__(predicts_classes)

        self.does_normalization = False
        """whether this tagger also performs normalization"""
        self.normalization_database = ''
        """additional info about the normalization database, e.g. URL"""

    def tag(self, dataset):
        """
        :type dataset: nalaf.structures.data.Dataset
        """
        import warnings
        warnings.warn('Use rather the method: annotate', DeprecationWarning)
        return self.annotate(dataset)

    @abc.abstractmethod
    def annotate(self, dataset):
        """
        :type dataset: nalaf.structures.data.Dataset
        """
        pass


class RelationExtractor(Annotator):
    """
    Abstract class for tagging a dataset with predicted relations between
    entities.

    Subclasses that inherit this class should:
    * Be named [Name]RelationExtractor
    * Implement the abstract method annotate
    * Use some sort of model or service to generate predictions
        * If you only want to read in predictions already saved in ann.json
          use AnnJsonAnnotationReader with _is_predicted = True
        * This will not only read the entities, but also the relations
    * Append new items to the list field "predicted_relations" of each Part in the dataset
    * Set the meta_attribute predicts_classes

    :type does_normalization: bool
    :type normalization_database: str
    :type predicts_classes: list[str]
    """
    def __init__(self, entity1_class, entity2_class, relation_type):
        super().__init__(relation_type)

        self.entity1_class = entity1_class
        """class id of the first entity"""
        self.entity2_class = entity2_class
        """class id of the second entity"""
        self.relation_type = relation_type
        """the type of relation between the two entiies in predicts_classes"""


    def tag(self, dataset):
        """
        :type dataset: nalaf.structures.data.Dataset
        """
        import warnings
        warnings.warn('Use rather the method: annotate', DeprecationWarning)
        return self.annotate(dataset)


    @abc.abstractmethod
    def annotate(self, dataset):
        """
        :type dataset: nalaf.structures.data.Dataset
        """
        pass


class StubRelationExtractor(RelationExtractor):
    """
    Stub RelationExtractor to mark as a true relationship all edges generated by the given `edge_generator`.

    See `StubSameSentenceRelationExtractor`, which is mere sugar code to use the edge generator that generates
    all edges (and therefore relationships) between all pairs of class-chosen entities contained in the same sentence.
    """

    def __init__(self, edge_generator, use_spacy_pipelines=False):
        super().__init__(edge_generator.entity1_class, edge_generator.entity2_class, edge_generator.relation_type)

        if use_spacy_pipelines:
            nlp = get_spacy_nlp_english(load_parser=True)
            self.sentence_splitter = GenericSplitter(lambda string: (sent.text for sent in nlp(string).sents))
            self.tokenizer = GenericTokenizer(lambda string: (tok.text for tok in nlp.tokenizer(string)))
        else:
            self.sentence_splitter = NLTK_SPLITTER
            self.tokenizer = NLTK_TOKENIZER

        self.edge_generator = edge_generator


    def tag(self, dataset):
        import warnings
        warnings.warn('Use the method: annotate', DeprecationWarning)
        return self.annotate(dataset)


    def annotate(self, dataset):
        self.sentence_splitter.split(dataset)
        self.tokenizer.tokenize(dataset)
        self.edge_generator.generate(dataset)

        for edge in dataset.edges():
            edge.pred_target = +1

        dataset.form_predicted_relations()


class StubSameSentenceRelationExtractor(StubRelationExtractor):

    def __init__(self, entity1_class, entity2_class, relation_type, use_gold=True, use_pred=True):
        edge_generator = SentenceDistanceEdgeGenerator(entity1_class, entity2_class, relation_type, distance=0, use_gold=use_gold, use_pred=use_pred)
        super().__init__(edge_generator)


    def annotate(self, dataset):
        super().annotate(dataset)


class StubSamePartRelationExtractor(StubRelationExtractor):

    def __init__(self, entity1_class, entity2_class, relation_type, use_gold=True, use_pred=True):
        edge_generator = SentenceDistanceEdgeGenerator(entity1_class, entity2_class, relation_type, distance=None, use_gold=use_gold, use_pred=use_pred)
        super().__init__(edge_generator)


    def annotate(self, dataset):
        super().annotate(dataset)
