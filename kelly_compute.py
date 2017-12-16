import pdb

file = open("aoke/statistics.txt",'r',encoding='UTF-8')
output = open(r'aoke/analysis.txt', 'w+',encoding='UTF-8')
setting = {
    'pay':1.9,
}
def get_kelly_rate(profit_rate):
    result = (profit_rate * setting['pay'] - (1 - profit_rate)) / setting['pay']
    return result

def output_analysis(league_name,kelly_rate,bet_rate):
    output_text = str(league_name)+ ': ' + str(kelly_rate) + ' ' + str(bet_rate)
    output.write(output_text)
    output.write("\n")

standard_kelly_rate = get_kelly_rate(0.5)

while 1:
    lines = file.readlines(100)
    if not lines:
        break
    for line in lines:
        league_info = line.strip().split(':')
        league_name = league_info[0]
        win_score = float(league_info[1].split(' ')[0])
        loss_score = float(league_info[1].split(' ')[1])
        kelly_rate = "%.2f%%" % (get_kelly_rate(win_score/(win_score+loss_score)) * 100)
        bet_rate = round(get_kelly_rate(win_score/(win_score+loss_score))/standard_kelly_rate,2)
        output_analysis(league_name, kelly_rate, bet_rate)

file.close()
output.close()