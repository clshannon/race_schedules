angular.module('racetrackapp')

    .controller('rtRacetrackListCtrl', function($scope, $location, rtRacetrackSvc) {

        //$scope.racetracks = rtRacetrackSvc.get();
        $scope.loading = true;
        
        rtRacetrackSvc.get(function(data) {
            // success handler
        	$scope.racetracks = data;
        	$scope.loading = false;
        }, function(error) {
            // error handler
        	$scope.loading = false;
        });
        
        $scope.distanceFilterOptions = [
                         {name: 'Select All', value:null},
                         {name: '10', value:10},
                         {name: '20', value:20},
                         {name: '50', value:50},
                         {name: '100', value:100},
                         {name: '200', value:200},
                         {name: '500', value:500}
                       ];
        $scope.distanceFilter = $scope.distanceFilterOptions[0];
        
        $scope.applyDistanceFilter = function() {
        	
        	$scope.loading = true;  
        	
        	if($scope.distanceFilter.value == null) {

                rtRacetrackSvc.get(function(data) {
                    // success handler
                	$scope.racetracks = data;
                	$scope.loading = false;
                }, function(error) {
                    // error handler
                	$scope.loading = false;
                });
        		
        	} else {
                
	        	rtRacetrackSvc.get({
	        		distance_filter:$scope.distanceFilter.value
	        	},function(data) {
	        	    // success handler
	            	$scope.racetracks = data;
	            	$scope.loading = false;
	        	}, function(error) {
	        	    // error handler
	            	$scope.loading = false;
	        	});
        		
        	}
        	
        }

    });