# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from ...utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_tensorflow_text_available,
    is_tokenizers_available,
    is_torch_available,
)


_import_structure = {
    "configuration_character_bert": [
        "CHARACTER_BERT_PRETRAINED_CONFIG_ARCHIVE_MAP",
        "CharacterBertConfig",
        "CharacterBertOnnxConfig",
    ],
    "tokenization_character_bert": ["BasicTokenizer", "CharacterBertTokenizer", "WordpieceTokenizer"],
}

try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_character_bert_fast"] = ["CharacterBertTokenizerFast"]

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_character_bert"] = [
        "CHARACTER_BERT_PRETRAINED_MODEL_ARCHIVE_LIST",
        "CharacterBertForMaskedLM",
        "CharacterBertForMultipleChoice",
        "CharacterBertForNextSentencePrediction",
        "CharacterBertForPreTraining",
        "CharacterBertForQuestionAnswering",
        "CharacterBertForSequenceClassification",
        "CharacterBertForTokenClassification",
        "CharacterBertLayer",
        # TODO: eventually add support for "CharacterBertLMHeadModel",
        "CharacterBertModel",
        "CharacterBertPreTrainedModel",
        "load_tf_weights_in_character_bert",
    ]

try:
    if not is_tensorflow_text_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_character_bert_tf"] = ["TFCharacterBertTokenizer"]

if TYPE_CHECKING:
    from .configuration_character_bert import (
        CHARACTER_BERT_PRETRAINED_CONFIG_ARCHIVE_MAP,
        CharacterBertConfig,
        CharacterBertOnnxConfig,
    )
    from .tokenization_character_bert import BasicTokenizer, CharacterBertTokenizer, WordpieceTokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_character_bert_fast import CharacterBertTokenizerFast

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_character_bert import (
            CHARACTER_BERT_PRETRAINED_MODEL_ARCHIVE_LIST,
            CharacterBertForMaskedLM,
            CharacterBertForMultipleChoice,
            CharacterBertForNextSentencePrediction,
            CharacterBertForPreTraining,
            CharacterBertForQuestionAnswering,
            CharacterBertForSequenceClassification,
            CharacterBertForTokenClassification,
            CharacterBertLayer,
            # CharacterBertLMHeadModel,
            CharacterBertModel,
            CharacterBertPreTrainedModel,
            load_tf_weights_in_character_bert,
        )

    try:
        if not is_tensorflow_text_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_character_bert_tf import TFCharacterBertTokenizer

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
