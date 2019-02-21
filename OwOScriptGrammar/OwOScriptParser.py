# Generated from OwOScript.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\7\3\27\n\3\f\3\16\3\32\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5)\n\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n")
        buf.write("\f\16\20\2\2\2:\2\22\3\2\2\2\4\30\3\2\2\2\6 \3\2\2\2\b")
        buf.write("(\3\2\2\2\n*\3\2\2\2\f-\3\2\2\2\16/\3\2\2\2\208\3\2\2")
        buf.write("\2\22\23\5\4\3\2\23\24\7\2\2\3\24\3\3\2\2\2\25\27\5\6")
        buf.write("\4\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\5\3\2\2\2\32\30\3\2\2\2\33\34\5\b\5\2\34\35")
        buf.write("\7\3\2\2\35!\3\2\2\2\36!\5\16\b\2\37!\5\20\t\2 \33\3\2")
        buf.write("\2\2 \36\3\2\2\2 \37\3\2\2\2!\7\3\2\2\2\")\5\n\6\2#)\5")
        buf.write("\f\7\2$%\7\4\2\2%&\5\b\5\2&\'\7\5\2\2\')\3\2\2\2(\"\3")
        buf.write("\2\2\2(#\3\2\2\2($\3\2\2\2)\t\3\2\2\2*+\7\6\2\2+,\7\20")
        buf.write("\2\2,\13\3\2\2\2-.\7\21\2\2.\r\3\2\2\2/\60\7\7\2\2\60")
        buf.write("\61\7\b\2\2\61\62\5\4\3\2\62\63\7\t\2\2\63\64\7\n\2\2")
        buf.write("\64\65\7\b\2\2\65\66\5\4\3\2\66\67\7\t\2\2\67\17\3\2\2")
        buf.write("\289\7\13\2\29:\7\b\2\2:;\5\4\3\2;<\7\t\2\2<\21\3\2\2")
        buf.write("\2\5\30 (")
        return buf.getvalue()


class OwOScriptParser ( Parser ):

    grammarFileName = "OwOScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'literal'", "'if'", 
                     "'{'", "'}'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMMENT", "LINE_COMMENT", 
                      "HASH_COMMENT", "WS", "SINGLE_DIGIT", "IDENTIFIER" ]

    RULE_script = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_number = 4
    RULE_command = 5
    RULE_ternary = 6
    RULE_whileloop = 7

    ruleNames =  [ "script", "statements", "statement", "expression", "number", 
                   "command", "ternary", "whileloop" ]

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
    COMMENT=10
    LINE_COMMENT=11
    HASH_COMMENT=12
    WS=13
    SINGLE_DIGIT=14
    IDENTIFIER=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 16
            self.statements()
            self.state = 17
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
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OwOScriptParser.T__1) | (1 << OwOScriptParser.T__3) | (1 << OwOScriptParser.T__4) | (1 << OwOScriptParser.T__8) | (1 << OwOScriptParser.IDENTIFIER))) != 0):
                self.state = 19
                self.statement()
                self.state = 24
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
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OwOScriptParser.T__1, OwOScriptParser.T__3, OwOScriptParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.expression()
                self.state = 26
                self.match(OwOScriptParser.T__0)
                pass
            elif token in [OwOScriptParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.ternary()
                pass
            elif token in [OwOScriptParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
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


        def command(self):
            return self.getTypedRuleContext(OwOScriptParser.CommandContext,0)


        def expression(self):
            return self.getTypedRuleContext(OwOScriptParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OwOScriptParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OwOScriptParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OwOScriptParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.number()
                pass
            elif token in [OwOScriptParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.command()
                pass
            elif token in [OwOScriptParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(OwOScriptParser.T__1)
                self.state = 35
                self.expression()
                self.state = 36
                self.match(OwOScriptParser.T__2)
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


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_DIGIT(self):
            return self.getToken(OwOScriptParser.SINGLE_DIGIT, 0)

        def getRuleIndex(self):
            return OwOScriptParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = OwOScriptParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(OwOScriptParser.T__3)
            self.state = 41
            self.match(OwOScriptParser.SINGLE_DIGIT)
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
        self.enterRule(localctx, 10, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(OwOScriptParser.IDENTIFIER)
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
        self.enterRule(localctx, 12, self.RULE_ternary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(OwOScriptParser.T__4)
            self.state = 46
            self.match(OwOScriptParser.T__5)
            self.state = 47
            self.statements()
            self.state = 48
            self.match(OwOScriptParser.T__6)
            self.state = 49
            self.match(OwOScriptParser.T__7)
            self.state = 50
            self.match(OwOScriptParser.T__5)
            self.state = 51
            self.statements()
            self.state = 52
            self.match(OwOScriptParser.T__6)
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
        self.enterRule(localctx, 14, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(OwOScriptParser.T__8)
            self.state = 55
            self.match(OwOScriptParser.T__5)
            self.state = 56
            self.statements()
            self.state = 57
            self.match(OwOScriptParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





