import React from 'react'
import './SearchField.scss';

const SearchField = () => {

    const setLocation = (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        window.localStorage.setItem("location", formData.get("location"));
    }

    return (
        <div style={{ display: "block", margin: "0 auto" }}>
            <input class="c-checkbox" type="checkbox" id="checkbox" />
            <div class="c-formContainer" style={{ margin: "0 auto" }}>
                <form class="c-form" onSubmit={setLocation}>
                    <input class="c-form__input" name="location" placeholder="Location" />
                    <button type="submit" class="c-form__button" style={{cursor: "pointer"}}>Set!</button>
                    <label class="c-form__toggle" for="checkbox" data-title="Where at? 🗺️"></label>
                </form>
            </div>
        </div>
    )
}

export default SearchField
