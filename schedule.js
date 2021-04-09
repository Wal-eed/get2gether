

const data = {
    name: "tim",
    id: 123,
    /**
     * When user selects the preset uni_timetable, it sums all th 
     */
    presets: [              // Not free (blocked off) times that are layered onto google cal
        uni_timetable: {
            start_date: ?,
            recurring: 7,
            blocked_times: [
                [],
                [],
                [],
                [],
                [],
                [],
                []
            ]
        }, 
        example_preset: {
            start_date:"9/10/2030",
            recurring: 0,              // <--- one-off, non-recurring
            blocked_times: [
                [],
                [],
            ]
        }
    ]
}




