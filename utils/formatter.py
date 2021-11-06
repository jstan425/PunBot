import disnake



def colour(*args):
    
    """Returns a discord Colour object.
    Pass one as an argument to define colour:
        `int` match colour value.
        `str` match common colour names.
        `disnake.Guild` bot's guild colour.
        `None` light grey.
    """
    
    arg = args[0] if args else None
    if isinstance(arg, int):
        return disnake.Colour(arg)
    if isinstance(arg, str):
        colour = arg
        try:
            return getattr(disnake.Colour, colour)()
        except AttributeError:
            return disnake.Colour.lighter_grey()
    if isinstance(arg, disnake.Guild):
        return arg.me.colour
    else:
        return disnake.Colour.lighter_grey()

def generate_embed(msg_type='',
               title=None, 
               icon=None,
               desc=None,
               msg_colour=None,
               title_url=None,
               thumbnail='',
               image='',
               fields=None,
               footer=None,
               footer_icon=None,
               inline=True
               ):
    
    """Returns a formatted discord embed object.
    Define either a type or a colour.
    Types are:
    error, warning, info, success, help.
    """
    
    embed_types = {
        'error':{
            'colour':0xEE4B2B
        },
        'warning':{
            'colour':0xFFD700
        },
        'info':{
            'colour':0x3094dd
        },
        'success':{
            'colour':0x66ff00
        },
        'help':{
            'colour':0xca00b9
        }
    }
    if msg_type in embed_types:
        msg_colour = embed_types[msg_type]['colour']
    elif not isinstance(msg_colour, disnake.Colour):
        msg_colour = colour(msg_colour) 
    embed = disnake.Embed(description=desc,
                          colour=msg_colour
                          )
    if not title_url:
        title_url = disnake.Embed.Empty
    if not icon:
        icon = disnake.Embed.Empty
    if title:
        embed.set_author(name=title,
                         icon_url=icon,
                         url=title_url
                         )
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if image:
        embed.set_image(url=image)
    if fields:
        for key, value in fields.items():
            ilf = inline
            if not isinstance(value, str):
                ilf = value[0]
                value = value[1]
            embed.add_field(name=key, value=value, inline=ilf)
    if footer:
        footer = {'text':footer}
        if footer_icon:
            footer['icon_url'] = footer_icon
        embed.set_footer(**footer)
    return embed