import React, { useState } from 'react';
import classNames from 'classnames';
import { SectionProps } from '../../utils/SectionProps';
import ButtonGroup from '../elements/ButtonGroup';
import Button from '../elements/Button';
import Image from '../elements/Image';
import Modal from '../elements/Modal';
import SearchField from '../chronicle/SearchField';
import FadeIn from 'react-fade-in';

import Timetable from '../chronicle/Timetable';

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
   */
  const [page, setPage] = useState("start");
  const [meetingName, setMeetingName] = useState(null);


  const startNewMeeting = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target); 
    setMeetingName(formData.get("meetingName"));
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
                
            {(page === "start") && (
              <FadeIn
                delay={600}
                transitionDuration={1000}
              >
                {/* <Ass /> */}
                <h1>
                  Get2Gether 🗨️
                </h1>
                <div className="container-xs">
                  <p>
                    When2Meet, <em>but not shit</em>. 
                    </p>
                  <div>
                    <SearchField startNewMeeting={startNewMeeting} />
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
                <Button color="primary" onClick={() => setPage("start")}>Back</Button>
                <Button color="primary" onClick={() => setPage("timetable")}>Next</Button>
              </FadeIn>
            )}
            {(page === "timetable") && (
              <FadeIn
                delay={400}
                transitionDuration={1000}
              >
                <Timetable />
                <Button color="primary" onClick={() => setPage("day-selection")}>Back</Button>
                <Button color="primary" onClick={() => setPage("invite")}>Next</Button>
              </FadeIn>
            )}
            {(page === "invite") && (
              <FadeIn
                delay={400}
                transitionDuration={1000}
              >
                <Button color="primary" onClick={() => setPage("start")}>Back to start</Button>
              </FadeIn>
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