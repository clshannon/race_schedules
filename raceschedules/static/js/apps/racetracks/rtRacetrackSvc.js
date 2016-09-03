angular.module('racetrackapp')
    .factory('rtRacetrackSvc', function($resource) {

    	var RacetrackResource = $resource('/api/racetracks/:id', {id: "@id"},{
    		'update': { method:'PUT' }
    	});  	
    	
    	return RacetrackResource;    	
    	
    })