import React from "react";
import PropTypes from "prop-types";


const ProfileTop = ({
  profile: { social ,avatar},
  user: { full_name },
}) => {


  return (
    <div className='profile-top bg-primary p-2'>
      <img className='round-img my-1' alt='' src={avatar}/>
      <h1 className='large'>{full_name}</h1>
      <div className='icons my-1'>
        {social
          ? Object.entries(social)
              .filter(([_, value]) => value)
              .map(([key, value]) => (
                <a
                  key={key}
                  href={value}
                  target='_blank'
                  rel='noopener noreferrer'
                >
                  <i className={`fab fa-${key} fa-2x`}></i>
                </a>
              ))
          : null}
      </div>
    </div>
  );
};

ProfileTop.propTypes = {
  profile: PropTypes.object.isRequired,
};

export default ProfileTop;
