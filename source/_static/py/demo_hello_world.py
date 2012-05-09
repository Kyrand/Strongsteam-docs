# -*- encoding: UTF-8
from strongsteam.clients import ss_client as ssc
from strongsteam.clients.ss_client import log

# set log to INFO if you want lots of progress information or
# use WARNING just to see the main client messages
log.setLevel(ssc.logging.WARNING)


if __name__ == "__main__":
    cli = ssc.StrongSteam()

    hello = cli.add_job(None, 'hello_world', data={'name':'oh, mighty Strongsteam user'})
    print hello.get_data()

