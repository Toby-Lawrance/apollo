import random

from discord.ext import commands
from discord.ext.commands import Context, Bot, clean_content

from utils.aliases import get_name_string

LONG_HELP_TEXT = """
Picks randomly between two options (or heads and tails if left blank)
"""

SHORT_HELP_TEXT = """Picks randomly between two options"""


class Flip(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(help=LONG_HELP_TEXT, brief=SHORT_HELP_TEXT)
    async def flip(self, ctx: Context, *args: clean_content):
        display_name = get_name_string(ctx.message)
        if len(args) == 1:
            await ctx.send(f"I can't flip just one item {display_name}! :confused:")
        else:
            options = ["Heads", "Tails"] if not args else args

            await ctx.send(f'{display_name}: {random.choice(options).lstrip("@")}')


def setup(bot: Bot):
    bot.add_cog(Flip(bot))
