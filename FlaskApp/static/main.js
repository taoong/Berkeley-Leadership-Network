(function () {

  'use strict';

  angular.module('webApp', [])

  .controller('webAppController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
    console.log("Angular")

     // fire the API request
    $scope.data = [];

    $scope.cleanData = function(responseData) {
        var cleanedData = []
        for(var i = 0; i < responseData['Location'].length; i++) {
            cleanedData[i] = {}
            for(var key in responseData) {
                cleanedData[i][key] = responseData[key][i].replace(/\b\w/g, l => l.toUpperCase());
            }
        }
        console.log(cleanedData);
        return cleanedData;
    };

    $scope.search = function(searchLocation, searchIndustry, searchJob) {
        return function (item) {
            if (searchLocation && !(item['Location'].includes(searchLocation))) {
                return false;
            }
            if (searchIndustry && !(item['Investment interest/sector'].includes(searchIndustry))) {
                return false;
            }
            if (searchJob && !(item['Primary Job Title'].includes(searchJob))) {
                return false;
            }
            return true;
        }
    };

    $http.post('/dataRequest').
      success(function(results) {
        console.log(results);
        $scope.data = $scope.cleanData(results);
        console.log($scope.data);
      }).
      error(function(error) {
        console.log(error);
      });

  }

  ]);

}());