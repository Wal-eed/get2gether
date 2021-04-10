import React from 'react'
import './SearchField.scss';

const SearchField = ({ startNewMeeting }) => {

    return (
        <div style={{ display: "block", margin: "0 auto" }}>
            <input class="c-checkbox" type="checkbox" id="location" />
            <div class="c-formContainer" style={{ margin: "0 auto" }}>
                <form class="c-form" onSubmit={startNewMeeting}>
                    <input class="c-form__input" name="meetingName" placeholder="Event name" />
                    <button type="submit" class="c-form__button" style={{cursor: "pointer"}}>Go!</button>
                    <label class="c-form__toggle" for="location" data-title="Make a plan ⌚"></label>
                </form>
            </div>
        </div>
    )
}

export default SearchField
