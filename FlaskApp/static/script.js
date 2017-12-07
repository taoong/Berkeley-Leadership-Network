data = [];

function getPeople() {
  $(function() {
        $.ajax({
            url: '/dataRequest',
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log(typeof(response));
                console.log(response.slice(700));
                var responseData = JSON.parse(response);
                console.log(responseData);
                for(var i = 0; i < responseData['Location'].length; i++) {
                    data[i] = {}
                    for(var key in responseData) {
                        data[i][key] = responseData[key][i]
                    }
                }
                console.log(data);
                for (var j = 0; j < 100; j++) {
                    var profile = $("<h2></h2>").text(data[j]["Full Name"].replace(/\b\w/g, l => l.toUpperCase()));
                    $("#description").append(profile);
                    status = "Position: "
                    var title = $("<p></p>").text(status.concat(data[j]["Primary Job Title"]));
                    $("#description").append(title);
                    sector = "Investment interest/sector: "
                    var interest = $("<p></p>").text(sector.concat(data[j]["Investment interest/sector"]));
                    $("#description").append(interest);
                    investing = "Actively Investing: "
                    var actively_investing = $("<p></p>").text(investing.concat(data[j]["Actively investing?"]));
                    $("#description").append(actively_investing);
                    sector = "Location: "
                    var location = $("<p></p>").text(sector.concat(data[j]["Location"]));
                    $("#description").append(location);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
  });
}

getPeople();