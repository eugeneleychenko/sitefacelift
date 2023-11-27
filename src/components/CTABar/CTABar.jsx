const CTABar = ({ ctaText, show, barHeight }) => {
    const barStyle = {
        height: barHeight,
        width: '100%',
        position: 'fixed', // Changed from 'relative' to 'fixed'
        top: show ? '0' : `-${barHeight}`, // Slide in effect
        left: 0,
        background: 'black',
        color: 'white',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 1000,
        opacity: show ? .7 : 0,
        transition: 'top 1s ease, opacity 1s ease', // Transition for top and opacity
        overflow: 'hidden'
    };

    return (
        <div style={barStyle}>
            {ctaText}
        </div>
    );
};

export default CTABar;