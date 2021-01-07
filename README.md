# How should I invest server

This is the server side to calculate the ideal portfolio. This is open as an API 
in case anyone is interested. 

# API

This server lives on [https://hsii-server.herokuapp.com](https://hsii-server.herokuapp.com).

### /calculate

To get the percentages ping the url 
` https://hsii-server.herokuapp.com/calculate`. <br><br>
The data should look as such: <br><br>
`
{
    values: {1:500,2:1500},
    percentages: {1:0.5,2:0.5},
    deposit: 5000
}
`
<br><br>
This means the current values are 500 and 1500 of product 1 and 2 respectively. The desired
percentages are 0.5 of both. The amount to be deposited is 5000. This will return a json.
<br>
<br>
`
{division_perc:[%f,%f]}
` 
<br><br>
Where %f will be the percentages by which to divide the deposit.