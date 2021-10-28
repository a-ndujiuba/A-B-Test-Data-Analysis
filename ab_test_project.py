import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Obtain 4 pie charts showing the different locationStep
# completions, and if they performed a searchCTA
# Plot bar chart with 3 bars, showing the different test variants,
# and if they performed a searchCTA - layer the bar charts to show %
# of entries that performed the searchCTA for each variant
# Boxplot to display the range of searches of venues
# for each variant
# Boxplot to display the range of enquiries for each variant
# Check whether budget est changed whether they sent enquiries
# Did using the app affect the number of searches or enquiries

# Function creating 4 piecharts showing the different location step
# completion statuses, and their proportion of each which completed a
# search CTA


def loc_step_pie(file, status):
    """Function to produce a pie chart displaying if users completed the
    search CTA, depending on the status of the completion of the
     location step during onboarding
     file: The csv file assigned to a variable, from which the data
     is obtained
     status: The status of completion of the user's onboarding"""

    loc_step_cta = file.groupby(['locationStep', 'searchCTA']).count()
    # Counting the number of users who have carried out the search CTA
    # for each location step completion status
    loc_step_cta.reset_index(inplace=True)
    # Index value for the new dataframe are being reset to allow
    # for iteration, without creating a new object
    x = loc_step_cta[(loc_step_cta['locationStep'] == status)]
    # The variable x is assigned to new dataframe, for the status of
    # location step that is inputted as an argument
    y = x.reset_index()
    # The variable y is assigned to this new data frame, with the
    # indexes again reset to allow for iteration
    if len(y) == 1:
        if y['searchCTA'][0] == 0:
            no_search = y['userId'][0]
            labels = ['No search']
            plt.pie(np.array([no_search]))
        else:
            search = y['userId'][0]
            labels = ['Search']
            plt.pie(np.array([search]))
    # If for a given location step status, we have only 0, or only 1
    # for the searchCTA, we look for what the value of that searchCTA
    # is, and plot the appropriate pie chart
    else:
        no_search = y['userId'][0]
        search = y['userId'][1]
        labels = ['No search', 'Search']

        plt.pie(np.array([no_search, search]))
    # If we have both 0 and 2 for the values of searchCTA for a given
    # location step status, we plot a pie graph for the two values
    plt.legend(labels, loc='best')
    plt.title(f'Location Step {status}')
    plt.show()
    print(loc_step_cta)
    print(y)


df = pd.read_csv('Bridebook - JDS - challengeData.1634657757.csv')
# loc_step_pie(df, 'seen')

# Code to produce 4 bars on a chart, displaying the average number of
# weekly enquiries sent to venues for each location step completion
# status

# venEnq_data = df.groupby(['locationStep']).mean()
# venEnq_data = venEnq_data.reset_index()
# y_variables = venEnq_data['venEnq']
# x_variables = venEnq_data['locationStep']
# plt.bar(x_variables, y_variables)
# plt.title('Location step completion against average number of weekly'
#           ' enquiries sent to venues', fontsize=20)
# plt.xlabel('Location step completion status', fontsize=16)
# plt.ylabel('Average number of venue enquiries per week', fontsize=16)
# plt.xticks(size=14)
# plt.yticks(size=14)
# plt.show()

# Code to produce the relationship between the searchCTA and the
# different test variants

no_of_entries = len(df)
# Obtains the length of the dataframe


def cta_count(file, v):
    """Function to obtain the number of users who completed a search
    CTA for each different variant group
    file: The variable upon which the dataframe is attached
    v: The test variant number"""
    count = 0
    # Initialise the count variable
    for a in range(0, no_of_entries):
        if file['testVariant'][a] == v:
            if file['searchCTA'][a] == 1:
                count += 1
                # If the test variant number along the a'th row is equal to
                # the input test variant argument, and the search CTA is
                # equal to 1, ie true, we add 1 to the count
            else:
                continue
        else:
            continue
    # print(count)
    return count


# var_0_cta = cta_count(df, 0)
# var_1_cta = cta_count(df, 1)
# var_2_cta = cta_count(df, 2)
#
# var_0 = df['testVariant'].value_counts()[0]
# var_1 = df['testVariant'].value_counts()[1]
# var_2 = df['testVariant'].value_counts()[2]
#
# var_0_percent = round((var_0_cta/var_0)*100)
# var_1_percent = round((var_1_cta/var_1)*100)
# var_2_percent = round((var_2_cta/var_2)*100)
#
# plot_data = pd.DataFrame({
#     "Search CTA Completed":[var_0_cta, var_1_cta, var_2_cta],
#     "Variant Group Total":[var_0, var_1, var_2]
#     },index = [0, 1, 2])
#
# ax = plot_data.plot(kind="bar")
# ax.set_title("Variant Search Completion", fontsize=18)
# ax.annotate(f"{var_0_percent}%", xy=(-0.25,var_0_cta+20))
# ax.annotate(f"{var_1_percent}%", xy=(0.75, var_1_cta+20))
# ax.annotate(f"{var_2_percent}%", xy=(1.75, var_2_cta+20))
#
# plt.show()
# print(var_0_cta)
# print(var_0)

#
# def venSearch_list(file, data):
#     # for the dataset given, find the venSearch value and put it in the column
#     vslist = []
#     var_index = file.testVariant[file.testVariant == data].index.tolist()
#     for x in var_index:
#         vslist == vslist.append(file['venSearch'][x])
#     return vslist
#
# var_0_venSearches = venSearch_list(df, 0)
# var_1_venSearches = venSearch_list(df, 1)
# var_2_venSearches = venSearch_list(df, 2)
#
# venSearches_data = {'0':var_0_venSearches,
#                     '1':var_1_venSearches,
#                     '2':var_2_venSearches}
#
# venSearches_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in venSearches_data.items() ]))
#
# boxplot = venSearches_df.boxplot()
# plt.ylim(-1, 20)
# plt.xlabel('Test Variant')
# plt.ylabel('Search performed by user in week 1')
# plt.title('Weekly searches per variant')
# plt.show()


# def venEnq_list(file, data):
#     # for the dataset given, find the venEnq value and put it in the column
#     vslist = []
#     var_index = file.testVariant[file.testVariant == data].index.tolist()
#     for x in var_index:
#         vslist == vslist.append(file['venEnq'][x])
#     return vslist
#
# var_0_venEnq = venEnq_list(df, 0)
# var_1_venEnq = venEnq_list(df, 1)
# var_2_venEnq = venEnq_list(df, 2)
#
# venEnq_data = {'0':var_0_venEnq,
#                     '1':var_1_venEnq,
#                     '2':var_2_venEnq}
#
# venEnq_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in venEnq_data.items() ]))
#
# boxplot = venEnq_df.boxplot()
# # plt.ylim(0.5, 0.5)
# plt.xlabel('Test Variant')
# plt.ylabel('Enquiries sent by user in week 1')
# plt.title('Weekly enquiries per variant')
# plt.show()


def added_city(file, v):
    count = 0
    for value in range(0, no_of_entries):
        if file['addedCity'][value] == v:
            count += 1
        else:
            continue
    print(count)
    return count


def added_city_cta(file, v):
    count = 0
    for value in range(0, no_of_entries):
        if file['addedCity'][value] == v:
            if file['searchCTA'][value] == 1:
                count +=1
            else:
                continue
        else:
            continue
    print(count)
    return count


add_city_0 = added_city(df, 0)
add_city_cta_0 = added_city_cta(df, 0)
add_city_1 = added_city(df, 1)
add_city_cta_1 = added_city_cta(df, 1)

add_city_0_percent = round((add_city_cta_0/add_city_0)*100)
add_city_1_percent = round((add_city_cta_1/add_city_1)*100)

plot_data_city = pd.DataFrame({
    "Performed Search CTA":[add_city_cta_0, add_city_cta_1],
    "Total users":[add_city_0, add_city_1]
    },index = ['City not added', 'City added'])

graph = plot_data_city.plot(kind='bar')
graph.annotate(f"{add_city_0_percent}%", xy=(-0.25, add_city_cta_0+20))
graph.annotate(f"{add_city_1_percent}%", xy=(0.75, add_city_cta_1+20))
plt.xticks(rotation=360)
plt.xlabel('"Added City" completion status')
plt.ylabel('Number of users')
plt.title("Added city relationship to search CTA")
plt.show()

