
const data = {
    name: "tim’s cool event",
    id: 123,
    users: {
        user_id_0: {
            is_organiser: true,
            answered_email: true,
            preferred_times: [1234],// preferred start time (all times are timestamps)
            free_schedule: {
                "09/04/2021": [1, 1, 1, 1, 0, 1, 1, 0],  // 24 elements [12:00am to 11:00pm] [0000 to 2300]
                "10/04/2021": [1, 1, 1, 1, 0, 1, 1, 0],
            }   
        }, // for users without an existing account we only add their user_id after they confirm it themselves
        user_id_1: {
            is_organiser: false,
            answered_email: true,
            preferred_times: [1234, 5678]
        },
        user_id_2: {
            is_organiser: false,
            answered_email: true,
            preferred_times: [1234, 5678]
        }
    },
    location: {
        link: "www.google.com",
        venue: "unsw",
        long: 123456.222,
        lat: 5678.222
    },
    best_possible_times: [123, 456, 789],   // Calculated based on current user's schedules using a scheduler algo, sorted in increasing order of suitability
    event_finalised: false                  
}
