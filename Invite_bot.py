@client.command(description="Invite")
async def invite(ctx):
    embed=discord.Embed(title="Invite")
    embed.add_field(name="invite", value="BOT-INVITE-LINK-HERE")
    await ctx.send(embed=embed)
    print ("invite elküldve!")
