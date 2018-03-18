"""This file provides the full wotw module"""

# pylint:disable=W,C,R

from .constants import (
    HIERARCHY,
    PREFIXES
)
from .utils import (
    HasDescendants,
    HasRepository,
    ObservesHierarchy
)
from .repo import (
    GitConfig,
    HasConfig,
    FlowPrelaunch,
    FlowPrefix,
    FlowBranch,
    FlowTag,
    FlowRemote,
    FlowWrangler
)
from .parsers import (
    ParserSink,
    ParserNode,
    ParserSource
)
from .components import (
    Argument,
    ArgumentGroup,
    Action,
    Subcommand,
    Command,
    ComponentInstance,
    ArgumentInstance,
    ArgumentGroupInstance,
    ActionInstance,
    SubcommandInstance,
    CommandInstance,
    BranchSubcommand
)
from .arguments import (
    BackMergeArgument,
    BaseArgument,
    BranchArgument,
    DefaultsArgument,
    DeleteArgument,
    DeleteLocalArgument,
    DeleteRemoteArgument,
    FetchArgument,
    FfArgument,
    FfMasterArgument,
    FileArgument,
    ForceArgument,
    GetArgument,
    GlobalArgument,
    HelpArgument,
    InteractiveArgument,
    KeepArgument,
    KeepLocalArgument,
    KeepRemoteArgument,
    LocalArgument,
    MessageArgument,
    MessageFileArgument,
    PreserveMergesArgument,
    PushArgument,
    PushDevelopArgument,
    PushMasterArgument,
    PushTagArgument,
    RebaseArgument,
    SetArgument,
    ShowCommandsArgument,
    SignArgument,
    SigningKeyArgument,
    SquashArgument,
    SystemArgument,
    TagArgument,
    TagNameArgument,
    VerboseArgument,
    BranchArgumentGroup,
    ConfigLocationArgumentGroup,
    PushArgumentGroup,
    TagArgumentGroup,
    UniversalArgumentGroup
)
from .actions import (
    BaseAction,
    CheckoutAction,
    DeleteAction,
    DiffAction,
    FinishAction,
    InitAction,
    ListAction,
    LogAction,
    PublishAction,
    RebaseAction,
    RenameAction,
    SetAction,
    StartAction,
    TrackAction,
    VersionAction
)
from .subcommands import (
    FeatureSubcommand,
    BugfixSubcommand,
    ReleaseSubcommand,
    HotfixSubcommand,
    SupportSubcommand,
    ConfigSubcommand
)
from .commands import WotwCommand
from .cli_file import cli
