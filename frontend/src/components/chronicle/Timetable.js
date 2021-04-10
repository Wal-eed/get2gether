import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './Timetable.scss';
import Button from '../elements/Button';
import Modal from '../elements/Modal';
import TimerangeSlider from './TimerangeSlider';



const Timetable = ({ isOrganiser, meetingName, defaultSchedule, participants=5, showLegend, modifiable=true, allowAutofill=false, setPage, canConfirmEvent=false, showTimeRange=true, showMap=false }) => {
    
    const defaultDays = [
        "",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ];
    
    const defaultTimes = [
        "12:00 am",
        "1:00 am",
        "2:00 am",
        "3:00 am",
        "4:00 am",
        "5:00 am",
        "6:00 am",
        "7:00 am",
        "8:00 am",
        "9:00 am",
        "10:00 am",
        "11:00 am",
        "12:00 pm",
        "1:00 pm",
        "2:00 pm",
        "3:00 pm",
        "4:00 pm",
        "5:00 pm",
        "6:00 pm",
        "7:00 pm",
        "8:00 pm",
        "9:00 pm",
        "10:00 pm",
        "11:00 pm"
    ];
    
    const [days, setDays] = useState(defaultDays);
    const [times, setTimes] = useState(defaultTimes);

    const [isMouseDown, setIsMouseDown] = useState(false);
    const [confirmEventModalActive, setConfirmEventModalActive] = useState(false);
    const [currDay, setCurrDay] = useState(null);
    const [currTime, setCurrTime] = useState(null);
    const [isScheduled, setIsScheduled] = useState(false);

    const [startTimeIndex, setStartTime] = useState(0);
    const [endTimeIndex, setEndTime] = useState(23);

    const openModal = (e) => {
        e.preventDefault();
        setConfirmEventModalActive(true);
    }

    const closeModal = (e) => {
        e.preventDefault();
        setConfirmEventModalActive(false);
    }   

    const adjustTimeRange = (start, end) => {
        // setDays(
        //     days.slice(startTimeIndex, endTimeIndex + 1)
        // )
        setStartTime(start);
        setEndTime(end);
        setTimes(
            defaultTimes.slice(startTimeIndex, endTimeIndex)
        );
    }    

    let timeMatrix = [];
    for (let i = 0; i < times.length; i++) {
        timeMatrix[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            timeMatrix[i][j] = 0;
        }
    }
    
    const unitHue = 255 / participants;
    console.log(unitHue);
    const hues = [];
    const opacities = [];
    for (let i = 0; i <= participants; i++) {
        hues.push(i * unitHue);
        opacities.push(1);
    }
    opacities[0] = 0.2;
    console.log(hues);
    
    const saveNewEventSchedule = (schedule) => {
        window.localStorage.setItem("schedule", JSON.stringify(schedule));
    }
    
    const overlayThisSchedule = (schedule) => {
        const oldSchedule = JSON.parse(window.localStorage.getItem("schedule"));
        for (let i = 0; i < times.length; i++) {
            for (let j = 0; j < days.length; j++) {
                oldSchedule[i][j] += schedule[i][j];
            }
        }
        window.localStorage.setItem("schedule", JSON.stringify(oldSchedule));
        setPage("everyone");
    }






    let autofillUnblockedSchedule = [];
    for (let i = 0; i < times.length; i++) {
        autofillUnblockedSchedule[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            autofillUnblockedSchedule[i][j] = 0;
        }
    }
    let workPreset = [];
    for (let i = 0; i < times.length; i++) {
        workPreset[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            workPreset[i][j] = 0;
        }
    }

    let uniPreset = [];
    for (let i = 0; i < times.length; i++) {
        uniPreset[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            uniPreset[i][j] = 0;
        }
    }


    const presets = [
        autofillUnblockedSchedule,
        workPreset,
        uniPreset,
    ]

    try {
        
        // POV: You are blocked on monday, tuesday, wednesday for these times:
        // Monday 
        autofillUnblockedSchedule[6][1] = 1;
        autofillUnblockedSchedule[7][1] = 1;
        autofillUnblockedSchedule[8][1] = 1;
        autofillUnblockedSchedule[9][1] = 1;
        autofillUnblockedSchedule[10][1] = 1;
        autofillUnblockedSchedule[11][1] = 1;
        autofillUnblockedSchedule[12][1] = 1;
        // Tuesday 
        autofillUnblockedSchedule[11][2] = 1;
        autofillUnblockedSchedule[12][2] = 1;
        autofillUnblockedSchedule[13][2] = 1;
        autofillUnblockedSchedule[14][2] = 1;
        autofillUnblockedSchedule[15][2] = 1;
        autofillUnblockedSchedule[16][2] = 1;
        autofillUnblockedSchedule[17][2] = 1;
        // Wednesday
        autofillUnblockedSchedule[11][3] = 1;
        autofillUnblockedSchedule[12][3] = 1;
        autofillUnblockedSchedule[13][3] = 1;
        autofillUnblockedSchedule[14][3] = 1;
        autofillUnblockedSchedule[15][3] = 1;
        autofillUnblockedSchedule[16][3] = 1;
        autofillUnblockedSchedule[17][3] = 1;
    
        // WORK PRESET
        // Monday 
        workPreset[6][1] = 1;
        workPreset[7][1] = 1;
        workPreset[8][1] = 1;
        workPreset[9][1] = 1;
        workPreset[10][1] = 1;
        workPreset[11][1] = 1;
        workPreset[12][1] = 1;
        workPreset[13][1] = 1;
        workPreset[14][1] = 1;
        workPreset[15][1] = 1;
        workPreset[16][1] = 1;
        workPreset[17][1] = 1;
        workPreset[18][1] = 1;
        // Tuesday 
        workPreset[6][2] = 1;
        workPreset[7][2] = 1;
        workPreset[8][2] = 1;
        workPreset[9][2] = 1;
        workPreset[10][2] = 1;
        workPreset[11][2] = 1;
        workPreset[12][2] = 1;
        workPreset[13][2] = 1;
        workPreset[14][2] = 1;
        workPreset[15][2] = 1;
        workPreset[16][2] = 1;
        workPreset[17][2] = 1;
        workPreset[18][2] = 1;
        // Wednesday 
        workPreset[6][3] = 1;
        workPreset[7][3] = 1;
        workPreset[8][3] = 1;
        workPreset[9][3] = 1;
        workPreset[10][3] = 1;
        workPreset[11][3] = 1;
        workPreset[12][3] = 1;
        workPreset[13][3] = 1;
        workPreset[14][3] = 1;
        workPreset[15][3] = 1;
        workPreset[16][3] = 1;
        workPreset[17][3] = 1;
        workPreset[18][3] = 1;
        // Thursday 
        workPreset[6][4] = 1;
        workPreset[7][4] = 1;
        workPreset[8][4] = 1;
        workPreset[9][4] = 1;
        workPreset[10][4] = 1;
        workPreset[11][4] = 1;
        workPreset[12][4] = 1;
        workPreset[13][4] = 1;
        workPreset[14][4] = 1;
        workPreset[15][4] = 1;
        workPreset[16][4] = 1;
        workPreset[17][4] = 1;
        workPreset[18][4] = 1;
        // Friday 
        workPreset[6][5] = 1;
        workPreset[7][5] = 1;
        workPreset[8][5] = 1;
        workPreset[9][5] = 1;
        workPreset[10][5] = 1;
        workPreset[11][5] = 1;
        workPreset[12][5] = 1;
        workPreset[13][5] = 1;
        workPreset[14][5] = 1;
        workPreset[15][5] = 1;
        workPreset[16][5] = 1;
        workPreset[17][5] = 1;
        workPreset[18][5] = 1;
    
        // Uni preset
        // Wednesday 
        uniPreset[6][3] = 1;
        uniPreset[7][3] = 1;
        uniPreset[8][3] = 1;
        uniPreset[9][3] = 1;
        uniPreset[10][3] = 1;
        uniPreset[11][3] = 1;
        uniPreset[16][3] = 1;
        uniPreset[17][3] = 1;
        uniPreset[18][3] = 1;
        // Friday 
        uniPreset[6][5] = 1;
        uniPreset[7][5] = 1;
        uniPreset[8][5] = 1;
        uniPreset[11][5] = 1;
        uniPreset[12][5] = 1;
        uniPreset[13][5] = 1;
        uniPreset[16][5] = 1;
        uniPreset[17][5] = 1;
        uniPreset[18][5] = 1;
    } catch {
        console.log("Lol.");
    }

    const autofill = (scheduleIndex) => {
        const preset = presets[scheduleIndex];
        for (let i = 0; i < times.length; i++) {
            for (let j = 0; j < days.length; ++j) {
                if (preset[i][j]) {
                    // This time is blocked. Do not add
                    schedule[i][j] = 0;
                } else {
                    schedule[i][j] = 1;
                }
            }
        }
        setSchedule([...schedule]);
        if (isOrganiser) {
            saveNewEventSchedule([...schedule]);

        }
    }


    const [schedule, setSchedule] = useState(defaultSchedule ? defaultSchedule : timeMatrix);

    const handleSelectTime = (row, col, force=false) => {
        if (modifiable) {
            if (isMouseDown || force) {
                let newTimeMatrix = [];
                for (let i = 0; i < times.length; i++) {
                    newTimeMatrix[i] = [...schedule[i]];            
                }
                newTimeMatrix[row][col] = (newTimeMatrix[row][col]) ? (0) : (1);
                setSchedule(newTimeMatrix);
                if (isOrganiser) {
                    saveNewEventSchedule(newTimeMatrix);
                }
            }
        }
    };

    const handleScheduleEvent = (event, row, col) => {
        if (canConfirmEvent) {
            openModal(event);
            setCurrDay(days[col]);
            setCurrTime(times[row]);
        }
    }

    return (
        <div>
            <div>
                {(!isScheduled) && (
                    <>
                        {showTimeRange && (
                            <>
                                <TimerangeSlider startTimeIndex={startTimeIndex} setStartTime={setStartTime} endTimeIndex={endTimeIndex} setEndTime={setEndTime} adjustTimeRange={adjustTimeRange} />
                                <div>
                                <span style={{margin: "20px"}}>
                                    {defaultTimes[startTimeIndex]}
                                </span>
                                -
                                <span style={{margin: "20px"}}>
                                    {defaultTimes[endTimeIndex]}
                                </span>
                                </div>
                            </>
                        )}
                        <table onMouseDown={() => setIsMouseDown(true)} onMouseUp={() => setIsMouseDown(false)}>
                            <thead>
                                <tr>
                                    {days.map(eachField => (
                                        <th className="noselect">
                                            {eachField}
                                        </th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {times.map((eachTime, row) => (
                                    <tr>
                                        <td className="noselect">
                                            {eachTime}
                                        </td>
                                        {days.map((_, col) => {
                                            if (col !== 0) {
                                                // if (schedule[row][col]) console.log("1");
                                                // console.log(schedule[row][col]);
                                                return (
                                                    <td 
                                                        // id={`time-${row}-${col}`} 
                                                        className={`time-brick noselect ${schedule[row][col] && "time-brick-selected"} ${!modifiable && "expanded-cell"}`} 
                                                        style={
                                                            (!modifiable) ? ({
                                                                backgroundColor: `rgba(0, ${hues[schedule[row][col]]}, 0, ${opacities[schedule[row][col]]})`  // WALEED COME HERE
                                                            }) : ({})
                                                        }
                                                        onMouseOver={() => handleSelectTime(row, col)}
                                                        onMouseDown={() => handleSelectTime(row, col, true)}
                                                        onClick={(e) => handleScheduleEvent(e, row, col)}
                                                    >
                                                        {/* {schedule[row][col]} */}
                                                    </td>
                                                );
                                            }
                                        })}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    {allowAutofill && (
                        <>
                            {/* <em>Availabilities synced from your Google Calendar</em>  */}
                            <Button color="primary" onClick={() => autofill(0)} style={{margin: "10px"}}>Auto-Fill From Calendar</Button> 
                            <Button color="primary" onClick={() => autofill(1)} style={{margin: "10px"}}>Work Preset</Button> 
                            <Button color="primary" onClick={() => autofill(2)} style={{margin: "10px"}}>Uni Preset</Button> 
                            {!isOrganiser && (
                                <Button color="info" onClick={() => overlayThisSchedule(schedule)} style={{margin: "10px"}}>Save</Button> 
                            )}
                        </>
                    )}
                    {showLegend && (
                        <div>
                            <h4 style={{textAlign: "left"}}>
                                Legend:
                            </h4>
                            <div style={{width: ((participants + 1) * 40) + "px", backgroundColor: "whitesmoke", height: "40px", borderRadius: "10px"}}>
                                {Array.from(Array(participants + 1).keys()).map(i => {
                                    return (
                                        <div style={{display: "inline-block", 
                                        width: "32px", 
                                        margin: "4px", 
                                        height: "30px", 
                                        backgroundColor: `rgb(0, ${hues[i]}, 0)`,  // WALEED COME HERE
                                        borderRadius: "10px"}}>
                                            {i}/{participants}
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                    )}
                    {(showMap) && (
                        <iframe
                            width="100%"
                            height="500px"
                            // style="border:0"
                            loading="lazy"
                            allowfullscreen
                            src={`https://www.google.com/maps/embed/v1/place?key=AIzaSyBjeL-5oS9102g1BbWRcmoAB2tx2tY_Au4&q=${window.localStorage.getItem("location") || "unsw"}`}
                        >
                        </iframe>
                    )}
                    <Modal
                        show={confirmEventModalActive}
                        handleClose={closeModal}
                    >
                        <h3>Scheduling <span className="glow">{meetingName}</span>:</h3>
                        <div>
                            Confirm for <strong>
                                {currDay}, {currTime}?
                            </strong>
                        </div>
                        <Button color="danger" style={{margin: "10px"}}>Cancel</Button>
                        <Button color="primary" onClick={() => {
                            setIsScheduled(true);
                        }} style={{margin: "10px"}}>
                            Confirm
                        </Button>
                    </Modal>
                </>
            )}
            {(isScheduled === true) && (
                <>
                  <h2>Done! 🎉</h2>
                  <div>
                    <span className="glow">{meetingName}</span> has been scheduled for <strong>{currDay}, {currTime}</strong>! 
                  </div>
                </>
            )}
            </div>
        </div>
    )
}

Timetable.propTypes = {

}

export default Timetable
