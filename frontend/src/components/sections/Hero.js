import React, { useState } from 'react';
import classNames from 'classnames';
import { SectionProps } from '../../utils/SectionProps';
import ButtonGroup from '../elements/ButtonGroup';
import Button from '../elements/Button';
import Image from '../elements/Image';
import Modal from '../elements/Modal';
import SearchField from '../chronicle/SearchField';

import glowStyles from './glow.scss';

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

  const [videoModalActive, setVideomodalactive] = useState(false);
  
  const [meetingName, setMeetingName] = useState(null);
  /**
   * 1. start
   * 2. day-selection
   * 3. timetable
   * 4. invite
   */
  const [page, setPage] = useState("invite");

  const openModal = (e) => {
    e.preventDefault();
    setVideomodalactive(true);
  }

  const closeModal = (e) => {
    e.preventDefault();
    setVideomodalactive(false);
  }   

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
              <>
                <h1 className="mt-0 mb-16 reveal-from-bottom" data-reveal-delay="200">
                  Get2Gether 🗨️
                </h1>
                <div className="container-xs">
                  <p className="m-0 mb-32 reveal-from-bottom" data-reveal-delay="400">
                    When2Meet, <em>but not shit</em>. 
                    </p>
                  <div className="reveal-from-bottom" data-reveal-delay="1000" style={{ marginTop: "200px" }} >
                    <SearchField startNewMeeting={startNewMeeting} />
                  </div>
                </div>
              </>
            )}
            {(page === "day-selection") && (
              <>
                <h3>
                  Select days for <span className="glow">
                    {meetingName}
                  </span>
                </h3>
                <Button color="primary" onClick={() => setPage("timetable")}>Next</Button>
              </>
            )}
            {(page === "timetable") && (
              <>
                <Button color="primary" onClick={() => setPage("invite")}>Next</Button>
              </>
            )}
            {(page === "invite") && (
              <>
                <Button color="primary" onClick={() => setPage("start")}>Back to start</Button>
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