from peopleofpi import PoliteiaClient, CommentExplorer
import pandas as pd
import json
from multiprocessing import Pool
from time import sleep

pi = PoliteiaClient("https://proposals.decred.org/api/v1")

def update_comments_csv():
    # Get all proposal comment votes dataframe
    all_tokens = pi.get_all_proposal_tokens()
    total_df = pd.DataFrame()
    print(f"Found tokens {all_tokens}")
    for proposal_token in all_tokens:
        total_df = total_df.append(pi.get_proposal_comments_votes_df(proposal_token))
    # Save Dataframe to CSV
    print("[WRITING]: Saving copy of raw comments DataFrame at all_comments.csv")
    total_df.to_csv("data/comments.csv")
    print("[SUCCESS]: Update succesful. Now exiting.")

def _get_user(username):
    user_id = pi.get_user_id(username)
    user_details = pi.get_user_details(user_id)
    # Get proposals
    # user_proposals = pi.get_user_proposals(user_id)
    # user_details['proposals'] = user_proposals
    return user_details

def update_users_csv():
    explorer = CommentExplorer('data/comments.csv')
    comments = explorer.comments_df
    ranking = explorer.ranking_from_comments(comments)
    # ACA VA EL MULTITHREAD
    # for username in ranking.username:
    #     users[username] = _get_user(username)

    pool = Pool(10)
    print(ranking.username)
    users = pool.map(_get_user, ranking.username)

    with open('data/users.json', 'w') as outfile:
        json.dump(users, outfile)    
    # users_df = pd.DataFrame(users)
    # users_df.to_csv("data/users.csv")


# Main Func
if __name__ == '__main__':
    while True:
        update_comments_csv()
        update_users_csv()
        print("[FINISHED UPDATING DB]: People of Politeia is ready to run.")
        sleep(3600)
    # bee = _get_user("bee")
    # print(bee)