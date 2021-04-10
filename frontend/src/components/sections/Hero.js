import React, { useState } from 'react';
import classNames from 'classnames';
import { SectionProps } from '../../utils/SectionProps';
import ButtonGroup from '../elements/ButtonGroup';
import Button from '../elements/Button';
import Image from '../elements/Image';
import Modal from '../elements/Modal';
import SearchField from '../chronicle/SearchField';
import FadeIn from 'react-fade-in';
import InviteSearchBar from '../chronicle/InviteSearchBar';
import LocationField from "../chronicle/LocationField";

import Timetable from '../chronicle/Timetable';
import DaysSelector from '../chronicle/DaysSelector';


import {
  FaCopy
} from 'react-icons/fa';

import './glow.scss';


const propTypes = {
  ...SectionProps.types
}

const defaultProps = {
  ...SectionProps.defaults
}


const Hero = ({
  className,
  topOuterDivider,
  bottomOuterDivider,
  topDivider,
  bottomDivider,
  hasBgColor,
  invertColor,
  username,
  setUsername,
  ...props
}) => {

  const outerClasses = classNames(
    'hero section center-content',
    topOuterDivider && 'has-top-divider',
    bottomOuterDivider && 'has-bottom-divider',
    hasBgColor && 'has-bg-color',
    invertColor && 'invert-color',
    className
  );

  const innerClasses = classNames(
    'hero-inner section-inner',
    topDivider && 'has-top-divider',
    bottomDivider && 'has-bottom-divider'
  );




  /**
   * 1. start
   * 2. day-selection
   * 3. timetable
   * 4. invite
   * 5. everyone - everyone's availabilites
   */
  const [page, setPage] = useState("start");
  const [meetingName, setMeetingName] = useState(window.localStorage.getItem("eventName") ? window.localStorage.getItem("eventName") : null);
  const [isOrganiser, setIsOrganiser] = useState(null);

  const startNewMeeting = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target); 
    setMeetingName(formData.get("meetingName"));
    window.localStorage.setItem("eventName", formData.get("meetingName"));
    setPage("day-selection");
  }

  return (
    <section
      {...props}
      className={outerClasses}
    >
      <div className="container-sm">
        <div className={innerClasses}>
          <div className="hero-content">

            {isOrganiser === null && (
              <>
                {window.localStorage.setItem("loggedIn", "")}
                <div>
                  Please select what you are:
                </div>
                <div>
                  <Button color="primary" onClick={() => {
                    setIsOrganiser(true);
                  }} style={{"margin": "10px"}}>Organiser</Button>
                  <Button color="primary" onClick={() => {
                    setIsOrganiser(false);
                  }} style={{"margin": "10px"}}>Attendee</Button>
                </div> 
              </>
            )}
            {/* ATTENDEE SCREENS */}
            {isOrganiser === false && (
              <>
                {page === "start" && (
                  <FadeIn
                    // delay={400}
                    // transitionDuration={1000}
                  >
                    <h3>Fill in your availability for <span className="glow">
                        {meetingName}
                      </span></h3>
                    <Timetable isOrganiser={isOrganiser} allowAutofill={true} setPage={setPage} />
                    <hr />
                  </FadeIn>
                )}
                {page === "everyone" && (
                  <FadeIn>
                    <h4>Thank you for submitting your availability for <span className="glow">
                        {meetingName}
                      </span>!</h4>
                    <hr />
                    <h3>Everyone's Availabilities</h3>
                    <Timetable defaultSchedule={JSON.parse(window.localStorage.getItem("schedule"))} isOrganiser={isOrganiser} participants={5} showLegend={true} modifiable={false} showTimeRange={false} />
                    <Button color="primary" onClick={() => window.location.reload()} style={{margin: "10px"}}>Back to start</Button>
                  </FadeIn>
                )}
              </>
            )}
            {/* ORGANISER SCREENS */}
            {isOrganiser === true && (
              <>
                {(page === "start") && (
                  <FadeIn
                    delay={600}
                    transitionDuration={1000}
                  >
                    <h1>
                      Get2Gether 📅
                    </h1>
                    <div className="container-xs">
                      <p>
                        "<strong><em style={{fontFamily: "Garamond"}}>Planning without the pain</em></strong>."
                      </p>
                      <div style={{marginTop: "150px"}}>
                        <SearchField startNewMeeting={startNewMeeting} />
                      </div>
                      <div style={{marginTop: "60px"}}>
                        <LocationField />
                      </div>
                    </div>
                  </FadeIn>
                )}
                {(page === "day-selection") && (
                  <FadeIn
                    delay={400}
                    transitionDuration={1000}
                  >
                    <h1>
                      Select days for <span className="glow">
                        {meetingName}
                      </span>
                    </h1>
                    <DaysSelector />
                    <div>
                      <Button color="primary" onClick={() => setPage("start")} style={{margin: "10px"}}>Back</Button>
                      <Button color="primary" onClick={() => setPage("timetable")} style={{margin: "10px"}}>Next</Button>
                    </div>
                  </FadeIn>
                )}
                {(page === "timetable") && (
                  <FadeIn
                    delay={400}
                    transitionDuration={1000}
                  >
                    <Timetable isOrganiser={isOrganiser} />
                    <div>
                      <Button color="primary" onClick={() => setPage("day-selection")} style={{margin: "10px"}}>Back</Button>
                      <Button color="primary" onClick={() => setPage("invite")} style={{margin: "10px"}}>Next</Button>
                    </div>
                  </FadeIn>
                )}
                {(page === "invite") && (
                  <FadeIn
                    delay={400}
                    transitionDuration={1000}
                  >
                    <h2>Share Invite Link:</h2>
                    <div style={{
                      height: "100px",
                      lineHeight: "100px",
                      textAlign: "center",
                    }}>
                      <span style={{
                        verticalAlign: "middle",
                        fontSize: "50px"
                      }}>
                        https://get2gether.com/qWe5Z 
                        <FaCopy className="copyButton" style={{
                          display: "inline-block", 
                          backgroundColor: "rgba(255, 255, 255, 0.25)", 
                          borderRadius: "50%", 
                          padding: "10px", 
                          width: "40px", 
                          height: "40px",
                          marginLeft: "20px"
                        }}/>
                      </span>
                    </div>
                    <div>
                      <InviteSearchBar />
                    </div>
                    <div>
                      <Button color="primary" onClick={() => window.location.reload()} style={{margin: "10px"}}>Back to start</Button>
                      <Button color="primary" onClick={() => setPage("everyone")} style={{margin: "10px"}}>View Responses</Button>
                    </div>
                  </FadeIn>
                )}
                {(page === "everyone") && (
                  <>
                    <Timetable meetingName={meetingName} defaultSchedule={JSON.parse(window.localStorage.getItem("schedule"))} isOrganiser={isOrganiser} participants={5} showLegend={true} modifiable={false} canConfirmEvent={true} showTimeRange={false} />
                    <Button color="primary" onClick={() => window.location.reload()} style={{margin: "10px"}}>Back to start</Button>
                  </>
                )}      
              </>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

Hero.propTypes = propTypes;
Hero.defaultProps = defaultProps;

export default Hero;
