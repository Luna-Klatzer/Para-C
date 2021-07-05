# coding=utf-8
""" Logic Tree Listener for the Para-C Pre-Processor """

from typing import TYPE_CHECKING
import antlr4

from .python import ParaCPreProcessorListener
from .ctx import FilePreProcessorContext
from .python import ParaCPreProcessorParser as parser

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    _p = parser.ParaCPreProcessorParser
    CompilationUnitContext = _p.CompilationUnitContext


# TODO! Add missing listener functions when grammar file was finished
class Listener(ParaCPreProcessorListener.ParaCPreProcessorListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCPreProcessorListener and then define the
    wanted behaviour inside the preprocessor processing.
    """

    def __init__(
            self,
            unit_ctx: CompilationUnitContext,
            file_stream: antlr4.FileStream
    ):
        self.file_ctx = FilePreProcessorContext()
        self.unit_ctx = unit_ctx
        self.file_stream = file_stream
        self._enable_out = False

    def walk_and_process_directives(self, enable_out: bool) -> str:
        """
        Walks through the passed compilation unit context and processing it,
        before then returning the newly generated file source code.

        :param enable_out: If set to True, warnings and errors will be logged
                           onto the console, but the errors won't be raised
        """
        self._enable_out = enable_out

        return self.process_directives()

    def process_directives(self) -> str:
        """ Processes the directives and generated the new source code """
        ...

    def gen_str(self) -> str:
        """
        Generated the new string of the file, where the directives where
        processed and the file was modified appropriately.
        """
        ...

    def enterCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by parser#compilationUnit.
        """
        ...

    def exitCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by parser#compilationUnit.
        """
        ...

    def enterTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by parser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by parser#translationUnit.
        """
        ...

    def enterExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Enter a parse tree produced by parser#externalItem.
        """
        ...

    def exitExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Exit a parse tree produced by parser#externalItem.
        """
        ...

    def enterCoreLanguageItem(
            self,
            ctx: _p.CoreLanguageItemContext
    ):
        """
        Enter a parse tree produced by parser#coreLanguageItem.
        """
        ...

    def exitCoreLanguageItem(
            self,
            ctx: _p.CoreLanguageItemContext
    ):
        """
        Exit a parse tree produced by parser#coreLanguageItem.
        """
        ...

    def enterPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def exitPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def enterLogicalPreProcessorDirective(
            self,
            ctx: _p.LogicalPreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#logicalPreProcessorDirective.
        """
        ...

    def exitLogicalPreProcessorDirective(
            self,
            ctx: _p.LogicalPreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#logicalPreProcessorDirective.
        """
        ...

    def enterStartSelectionBlock(
            self,
            ctx: _p.StartSelectionBlockContext
    ):
        """
        Enter a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def exitStartSelectionBlock(
            self,
            ctx: _p.StartSelectionBlockContext
    ):
        """
        Exit a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def enterLogicalDirectiveAlternatives(
            self,
            ctx: _p.LogicalDirectiveAlternativesContext
    ):
        """
        Enter a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def exitLogicalDirectiveAlternatives(
            self,
            ctx: _p.LogicalDirectiveAlternativesContext
    ):
        """
        Exit a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def enterLogicalElseDirective(
            self,
            ctx: _p.LogicalElseDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def exitLogicalElseDirective(
            self,
            ctx: _p.LogicalElseDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def enterIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#includeDirective.
        """
        ...

    def exitIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#includeDirective.
        """
        ...

    def enterFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def exitFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def enterComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def exitComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#computedIncludeDirective.
        """
        ...
