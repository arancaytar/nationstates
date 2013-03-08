## ABOUT

This is a client implementation of the XML API of the game NationStates 
(http://www.nationstates.net), allowing different queries on the game data.

## FEATURES

Aside from a library that allows general queries, this client comes with
multiple scripts for specific purposes, such as building a regional map of 
endorsements.

The client automatically throttles itself to at most fifty queries in thirty 
seconds. Note that this throttling is only done on a per-thread basis, so only 
one instance of the client may run simultaneously; your address will otherwise
be temporarily blocked by the NationStates server.

## LICENSE

This code is available under the GNU General Public License, v3 and later.

http://www.gnu.org/licenses/gpl-3.0.txt
