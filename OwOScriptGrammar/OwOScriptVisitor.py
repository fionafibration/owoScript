# Generated from OwOScript.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OwOScriptParser import OwOScriptParser
else:
    from OwOScriptParser import OwOScriptParser

# This class defines a complete generic visitor for a parse tree produced by OwOScriptParser.

class OwOScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OwOScriptParser#script.
    def visitScript(self, ctx:OwOScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#statements.
    def visitStatements(self, ctx:OwOScriptParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#statement.
    def visitStatement(self, ctx:OwOScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#expression.
    def visitExpression(self, ctx:OwOScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#number.
    def visitNumber(self, ctx:OwOScriptParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#command.
    def visitCommand(self, ctx:OwOScriptParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#ternary.
    def visitTernary(self, ctx:OwOScriptParser.TernaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OwOScriptParser#whileloop.
    def visitWhileloop(self, ctx:OwOScriptParser.WhileloopContext):
        return self.visitChildren(ctx)



del OwOScriptParser