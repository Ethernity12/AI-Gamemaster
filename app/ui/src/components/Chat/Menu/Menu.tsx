import styles from './Menu.module.scss';
import Separator from '../../Common/Separator/Separator';

function Menu () {
    return (
        <div className={styles.menuContainer}>
            <div className={styles.menuSettings}>
                Menu Settings
            </div>
            <Separator/>
            <div className={styles.menuItem}>
                Menu Item 1
            </div>
            <div className={styles.menuItem}>
                Menu Item 2
            </div>
            <div className={styles.menuItem}>
                Menu Item 3 
            </div>
        </div>
    )
}

export default Menu