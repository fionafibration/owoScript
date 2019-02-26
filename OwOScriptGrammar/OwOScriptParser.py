# Generated from OwOScript.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\3\6\3\"\n\3\r\3\16\3#\3\4\7\4\'")
        buf.write("\n\4\f\4\16\4*\13\4\3\5\3\5\3\5\3\5\3\5\5\5\61\n\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6\67\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\3\3")
        buf.write("\2\4\6\2S\2\34\3\2\2\2\4!\3\2\2\2\6(\3\2\2\2\b\60\3\2")
        buf.write("\2\2\n\66\3\2\2\2\f8\3\2\2\2\16;\3\2\2\2\20>\3\2\2\2\22")
        buf.write("@\3\2\2\2\24B\3\2\2\2\26E\3\2\2\2\30K\3\2\2\2\32T\3\2")
        buf.write("\2\2\34\35\5\6\4\2\35\36\5\4\3\2\36\37\7\2\2\3\37\3\3")
        buf.write("\2\2\2 \"\5\b\5\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2")
        buf.write("\2\2$\5\3\2\2\2%\'\5\26\f\2&%\3\2\2\2\'*\3\2\2\2(&\3\2")
        buf.write("\2\2()\3\2\2\2)\7\3\2\2\2*(\3\2\2\2+,\5\n\6\2,-\7\3\2")
        buf.write("\2-\61\3\2\2\2.\61\5\30\r\2/\61\5\32\16\2\60+\3\2\2\2")
        buf.write("\60.\3\2\2\2\60/\3\2\2\2\61\t\3\2\2\2\62\67\5\f\7\2\63")
        buf.write("\67\5\16\b\2\64\67\5\22\n\2\65\67\5\24\13\2\66\62\3\2")
        buf.write("\2\2\66\63\3\2\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\13\3")
        buf.write("\2\2\289\t\2\2\29:\7\23\2\2:\r\3\2\2\2;<\7\7\2\2<=\5\20")
        buf.write("\t\2=\17\3\2\2\2>?\7\24\2\2?\21\3\2\2\2@A\7\26\2\2A\23")
        buf.write("\3\2\2\2BC\7\26\2\2CD\7\b\2\2D\25\3\2\2\2EF\7\t\2\2FG")
        buf.write("\7\26\2\2GH\7\n\2\2HI\5\4\3\2IJ\7\13\2\2J\27\3\2\2\2K")
        buf.write("L\7\f\2\2LM\7\n\2\2MN\5\4\3\2NO\7\13\2\2OP\7\r\2\2PQ\7")
        buf.write("\n\2\2QR\5\4\3\2RS\7\13\2\2S\31\3\2\2\2TU\7\16\2\2UV\7")
        buf.write("\n\2\2VW\5\4\3\2WX\7\13\2\2X\33\3\2\2\2\6#(\60\66")
        return buf.getvalue()


class OwOScriptParser ( Parser ):

    grammarFileName = "OwOScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'literal'", "'lit'", "'l'", "'number'", 
                     "'()'", "'func'", "'{'", "'}'", "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "LINE_COMMENT", "HASH_COMMENT", 
                      "WS", "SINGLE_HEX_DIGIT", "NUMBER", "DECIMAL_INTEGER", 
                      "IDENTIFIER" ]

    RULE_script = 0
    RULE_statements = 1
    RULE_definitions = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_number = 5
    RULE_bignumber = 6
    RULE_integer = 7
    RULE_command = 8
    RULE_functioncall = 9
    RULE_definition = 10
    RULE_ternary = 11
    RULE_whileloop = 12

    ruleNames =  [ "script", "statements", "definitions", "statement", "expression", 
                   "number", "bignumber", "integer", "command", "functioncall", 
                   "definition", "ternary", "whileloop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    COMMENT=13
    LINE_COMMENT=14
    HASH_COMMENT=15
    WS=16
    SINGLE_HEX_DIGIT=17
    NUMBER=18
    DECIMAL_INTEGER=19
    IDENTIFIER=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definitions(self):
            return self.getTypedRuleContext(OwOScriptParser.DefinitionsContext,0)


        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(OwOScriptParser.EOF, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_script

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = OwOScriptParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.definitions()
            self.state = 27
            self.statements()
            self.state = 28
            self.match(OwOScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = OwOScriptParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OwOScriptParser.T__1) | (1 << OwOScriptParser.T__2) | (1 << OwOScriptParser.T__3) | (1 << OwOScriptParser.T__4) | (1 << OwOScriptParser.T__9) | (1 << OwOScriptParser.T__11) | (1 << OwOScriptParser.IDENTIFIER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.DefinitionContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_definitions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitions" ):
                return visitor.visitDefinitions(self)
            else:
                return visitor.visitChildren(self)




    def definitions(self):

        localctx = OwOScriptParser.DefinitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OwOScriptParser.T__6:
                self.state = 35
                self.definition()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OwOScriptParser.ExpressionContext,0)


        def ternary(self):
            return self.getTypedRuleContext(OwOScriptParser.TernaryContext,0)


        def whileloop(self):
            return self.getTypedRuleContext(OwOScriptParser.WhileloopContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OwOScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OwOScriptParser.T__1, OwOScriptParser.T__2, OwOScriptParser.T__3, OwOScriptParser.T__4, OwOScriptParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(OwOScriptParser.T__0)
                pass
            elif token in [OwOScriptParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.ternary()
                pass
            elif token in [OwOScriptParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.whileloop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(OwOScriptParser.NumberContext,0)


        def bignumber(self):
            return self.getTypedRuleContext(OwOScriptParser.BignumberContext,0)


        def command(self):
            return self.getTypedRuleContext(OwOScriptParser.CommandContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(OwOScriptParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OwOScriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.bignumber()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.command()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_HEX_DIGIT(self):
            return self.getToken(OwOScriptParser.SINGLE_HEX_DIGIT, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = OwOScriptParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OwOScriptParser.T__1) | (1 << OwOScriptParser.T__2) | (1 << OwOScriptParser.T__3))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(OwOScriptParser.SINGLE_HEX_DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BignumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(OwOScriptParser.IntegerContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_bignumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBignumber" ):
                return visitor.visitBignumber(self)
            else:
                return visitor.visitChildren(self)




    def bignumber(self):

        localctx = OwOScriptParser.BignumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bignumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(OwOScriptParser.T__4)
            self.state = 58
            self.integer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(OwOScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = OwOScriptParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(OwOScriptParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = OwOScriptParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(OwOScriptParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_functioncall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = OwOScriptParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(OwOScriptParser.IDENTIFIER)
            self.state = 65
            self.match(OwOScriptParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OwOScriptParser.IDENTIFIER, 0)

        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = OwOScriptParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(OwOScriptParser.T__6)
            self.state = 68
            self.match(OwOScriptParser.IDENTIFIER)
            self.state = 69
            self.match(OwOScriptParser.T__7)
            self.state = 70
            self.statements()
            self.state = 71
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OwOScriptParser.StatementsContext)
            else:
                return self.getTypedRuleContext(OwOScriptParser.StatementsContext,i)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_ternary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernary" ):
                return visitor.visitTernary(self)
            else:
                return visitor.visitChildren(self)




    def ternary(self):

        localctx = OwOScriptParser.TernaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ternary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(OwOScriptParser.T__9)
            self.state = 74
            self.match(OwOScriptParser.T__7)
            self.state = 75
            self.statements()
            self.state = 76
            self.match(OwOScriptParser.T__8)
            self.state = 77
            self.match(OwOScriptParser.T__10)
            self.state = 78
            self.match(OwOScriptParser.T__7)
            self.state = 79
            self.statements()
            self.state = 80
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileloopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(OwOScriptParser.StatementsContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_whileloop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileloop" ):
                return visitor.visitWhileloop(self)
            else:
                return visitor.visitChildren(self)




    def whileloop(self):

        localctx = OwOScriptParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(OwOScriptParser.T__11)
            self.state = 83
            self.match(OwOScriptParser.T__7)
            self.state = 84
            self.statements()
            self.state = 85
            self.match(OwOScriptParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





