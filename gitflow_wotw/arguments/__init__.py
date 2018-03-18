# pylint:disable=W,C,R

from .back_merge_argument import BackMergeArgument
from .base_argument import BaseArgument
from .branch_argument import BranchArgument
from .defaults_argument import DefaultsArgument
from .delete_argument import DeleteArgument
from .delete_local_argument import DeleteLocalArgument
from .delete_remote_argument import DeleteRemoteArgument
from .fetch_argument import FetchArgument
from .ff_argument import FfArgument
from .ff_master_argument import FfMasterArgument
from .file_argument import FileArgument
from .force_argument import ForceArgument
from .get_argument import GetArgument
from .global_argument import GlobalArgument
from .help_argument import HelpArgument
from .interactive_argument import InteractiveArgument
from .keep_argument import KeepArgument
from .keep_local_argument import KeepLocalArgument
from .keep_remote_argument import KeepRemoteArgument
from .local_argument import LocalArgument
from .message_argument import MessageArgument
from .message_file_argument import MessageFileArgument
from .preserve_merges_argument import PreserveMergesArgument
from .push_argument import PushArgument
from .push_develop_argument import PushDevelopArgument
from .push_master_argument import PushMasterArgument
from .push_tag_argument import PushTagArgument
from .rebase_argument import RebaseArgument
from .set_argument import SetArgument
from .show_commands_argument import ShowCommandsArgument
from .sign_argument import SignArgument
from .signing_key_argument import SigningKeyArgument
from .squash_argument import SquashArgument
from .system_argument import SystemArgument
from .tag_argument import TagArgument
from .tag_name_argument import TagNameArgument
from .verbose_argument import VerboseArgument

from .groups import (
    BranchArgumentGroup,
    ConfigLocationArgumentGroup,
    PushArgumentGroup,
    TagArgumentGroup,
    UniversalArgumentGroup
)
