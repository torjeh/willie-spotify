#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from willie import module
import spotimeta

@module.rule('(?u).*(spotify:(album|track|artist):([a-zA-Z0-9]{22})).*')
def hi(bot, trigger):
    #bot.say("It works, stupid ...: (" + trigger + ")")

    arr = trigger.split()
    for alt in arr:
       if unicode(alt).startswith(u'spotify'):
           spotifyUri = alt
    try:
        result = spotimeta.lookup(spotifyUri)
        nick = trigger.nick
        media = spotifyUri.split(":")[1]
        if media == 'album' or media == 'track':
            artist = result["result"]["artist"]["name"]
            track = result["result"]["name"]
            bot.say(nick + ' wants you to listen to the ' + media + " " + artist + " - " + track)
        else:
            bot.say(nick + ' wants you to listen to the artist ' + result["result"]["name"])
    except Exception:
        pass
