#include "SimMuon/CSCDigitizer/src/CSCDriftSim.h"
#include <cmath>
#include <iostream>

// the following functions were all generated by f2c.

double CSCDriftSim::avgPathLengthLowB() {

    static  const double coeff[7] = { .28872209,.21705601,.063908389,-.012224924,
            .012901814,-.0089355058,-.015769145 };

    // System generated locals
    float ret_val;

    // Local variables
    double x10, x11, x12, x13, x20, x21, x22;

/* ! Parameterization of drift path length - low field chambers */
/* ***********************************************************************
 */
/* DOC MC_BHGH_SLEN                                                      *
 */
/*                                                                      *
*/
/* DOC  Function    : Parameterization of the drift path length          *
 */
/* DOC                in the muon endcap CSCs.                           *
 */
/*                                                                      *
*/
/* DOC  References  : None                                               *
 */
/*                                                                      *
*/
/* DOC  Arguments   : YCELL - distance from the anode wire in the        *
 */
/*                           anode-cathode coordinate plane             *
*/
/* DOC                ZCELL - distance from the anode wire in the wire   *
 */
/*                           plane coordinate                           *
*/
/* DOC  Errors      : None                                               *
 */
/*                                                                      *
*/
/* DOC  Returns     : Drift path length for low field CSC chambers      *
*/
/*                                                                      *
*/
/* DOC  Created     : 15-OCT-1996   Author : Jeff Rowe                   *
 */
/* ***********************************************************************
 */


    x10 = 1.;
    x11 = fabs(ycell) * 2. - 1.;
    x12 = x11 * 2. * x11 - x10;
    x13 = x11 * 2. * x12 - x11;
    x20 = 1.;
    x21 = fabs(zcell) * 2. - 1.;
    x22 = x21 * 2. * x21 - x20;
    ret_val = coeff[0] + coeff[1] * x11 + coeff[2] * x21 + coeff[3] * x12 *
            x22 + coeff[4] * x22 + coeff[5] * x13 + coeff[6] * x11 * x21;
    return ret_val;
}


double CSCDriftSim::pathSigmaLowB() {
    /* Initialized data */

    static  const double coeff[12] = { .002854441,8.701339e-4,.0053064193,
            .0012356508,9.8627318e-4,.0013802449,-5.4633755e-4,.0026078648,
            .0044171026,6.2029063e-4,.0011392474,-.0056275595 };

    /* System generated locals */
    float ret_val;

    /* Local variables */
    double /*x10,*/ x11, x12, x13, x14, x15, x16, /*x20,*/ x21, x22, x23,
            x24, x25, x26, x27, x28, x29, x210, x211, x212, x213;

/* ! Parameterization of path length dispersion- low field chambers */
/* ***********************************************************************
 */
/* DOC MC_BHGH_SSIG                                                      *
 */
/*                                                                      *
*/
/* DOC  Function    : Parameterization of the drift path length          *
 */
/* DOC                dispersion in the muon endcap CSCs.                *
 */
/*                                                                      *
*/
/* DOC  References  : None                                               *
 */
/*                                                                      *
*/
/* DOC  Arguments   : YCELL - distance from the anode wire in the        *
 */
/*                           anode-cathode coordinate plane             *
*/
/* DOC                ZCELL - distance from the anode wire in the wire   *
 */
/*                           plane coordinate                           *
*/
/*           **NOTE** Both distances normalize to cell dim=1x1          *
*/
/* DOC  Errors      : None                                               *
 */
/*                                                                      *
*/
/* DOC  Returns     : Path length dispersion for low field CSC chambers *
*/
/*                                                                      *
*/
/* DOC  Created     : 15-OCT-1996   Author : Jeff Rowe                   *
 */
/* ***********************************************************************
 */


    //x10 = 1.; //not used later
    x11 = fabs(ycell) * 2. - 1.;
    x12 = x11 * x11;
    x13 = x11 * x12;
    x14 = x11 * x13;
    x15 = x11 * x14;
    x16 = x11 * x15;
    //x20 = 1.; //not used later
    x21 = fabs(zcell) * 2. - 1.;
    x22 = x21 * x21;
    x23 = x21 * x22;
    x24 = x21 * x23;
    x25 = x21 * x24;
    x26 = x21 * x25;
    x27 = x21 * x26;
    x28 = x21 * x27;
    x29 = x21 * x28;
    x210 = x21 * x29;
    x211 = x21 * x210;
    x212 = x21 * x211;
    x213 = x21 * x212;
    ret_val = coeff[0] + coeff[1] * x23 + coeff[2] * x24 + coeff[3] * x13 +
            coeff[4] * x11 * x21 + coeff[5] * x11 * x22 + coeff[6] * x16 +
            coeff[7] * x213 + coeff[8] * x212 + coeff[9] * x21 + coeff[10] *
            x11 * x23 + coeff[11] * x26;

    return ret_val;
}


double CSCDriftSim::avgDriftTimeLowB() {
    /* Initialized data */

    static const double coeff[20] = { 42.981588,25.732805,26.539129,16.719016,
            10.862044,7.4859085,5.0353142,3.3620548,1.9057762,2.2207695,
            -2.6787582,1.2977292,-.8358091,1.2452612,.74813469,-.57581194,
            .32705275,-.85426489,-.55688158,-.38384903 };

    /* System generated locals */
    float ret_val;

    /* Local variables */
    double x10, x11, x12, x13, x14, x20, x21, x22, x23, x24, x25,
            x26, x27, x28, x29;

/* ! Parameterization of drift time - low field chambers */
/* ***********************************************************************
 */
/* DOC MC_BLOW_TIME                                                      *
 */
/*                                                                      *
*/
/* DOC  Function    : Parameterization of the drift time                 *
 */
/* DOC                in the muon endcap CSCs.                           *
 */
/*                                                                      *
*/
/* DOC  References  : None                                               *
 */
/*                                                                      *
*/
/* DOC  Arguments   : YCELL - distance from the anode wire in the        *
 */
/*                           anode-cathode coordinate plane             *
*/
/*                           (ycell=1 > d_acat)                         *
*/
/* DOC                ZCELL - distance from the anode wire in the wire   *
 */
/*                           plane coordinate (zcell=1 > d_anod/2.)     *
*/
/* DOC  Errors      : None                                               *
 */
/*                                                                      *
*/
/* DOC  Returns     : Drift time for low field CSC chambers              *
 */
/*                                                                      *
*/
/* DOC  Created     : 15-OCT-1996   Author : Jeff Rowe                   *
 */
/* ***********************************************************************
 */




    x10 = 1.;
    x11 = fabs(ycell) * 2. - 1.;
    x12 = x11 * 2. * x11 - x10;
    x13 = x11 * 2. * x12 - x11;
    x14 = x11 * 2. * x13 - x12;
    x20 = 1.;
    x21 = fabs(zcell) * 2. - 1.;
    x22 = x21 * 2. * x21 - x20;
    x23 = x21 * 2. * x22 - x21;
    x24 = x21 * 2. * x23 - x22;
    x25 = x21 * 2. * x24 - x23;
    x26 = x21 * 2. * x25 - x24;
    x27 = x21 * 2. * x26 - x25;
    x28 = x21 * 2. * x27 - x26;
    x29 = x21 * 2. * x28 - x27;

    ret_val = coeff[0] + coeff[1] * x11 + coeff[2] * x21 + coeff[3] * x22 +
            coeff[4] * x23 + coeff[5] * x24 + coeff[6] * x25 + coeff[7] * x26
            + coeff[8] * x12 + coeff[9] * x27 + coeff[10] * x11 * x21 + coeff[
            11] * x28 + coeff[12] * x13 + coeff[13] * x12 * x21 + coeff[14] *
            x29 + coeff[15] * x13 * x21 + coeff[16] * x14 + coeff[17] * x11 *
            x22 + coeff[18] * x11 * x23 + coeff[19] * x11 * x24;
    return ret_val;
}


double CSCDriftSim::driftTimeSigmaLowB() {
    /* Initialized data */

    static  const double coeff[19] = { 6.2681223,3.5916437,5.5425809,4.6974052,
            3.8472392,3.1019155,2.4323913,1.8695623,1.3909068,.99056625,
            .52066638,.64671229,.68023389,.40512251,.40202738,.23908531,
            -.41245784,-.32196924,-.29890696 };

    /* Local variables */
    double /*x10,*/ x11, x20, x21, x22, x23, x24, x25, x26, x27, x28,
      x29, x210, x211, x212;

/* ! Parameterization of drift time dispersion- low field chambers */
/* ***********************************************************************
 */
/* DOC MC_BHGH_TSIG                                                      *
 */
/*                                                                      *
*/
/* DOC  Function    : Parameterization of the drift time dispersion      *
 */
/* DOC                in the muon endcap CSCs.                           *
 */
/*                                                                      *
*/
/* DOC  References  : None                                               *
 */
/*                                                                      *
*/
/* DOC  Arguments   : YCELL - distance from the anode wire in the        *
 */
/*                           anode-cathode coordinate plane             *
*/
/*                           (ycell=1 > d_acat)                         *
*/
/* DOC                ZCELL - distance from the anode wire in the wire   *
 */
/*                           plane coordinate (zcell=1 > d_anod/2.)     *
*/
/* DOC  Errors      : None                                               *
 */
/*                                                                      *
*/
/* DOC  Returns     : Drift time dispersion for low field CSC chambers   *
 */
/*                                                                      *
*/
/* DOC  Created     : 15-OCT-1996   Author : Jeff Rowe                   *
 */
/* ***********************************************************************
 */



    //x10 = 1.; //not used
    x11 = fabs(ycell) * 2. - 1.;
    x20 = 1.;
    x21 = fabs(zcell) * 2. - 1.;
    x22 = x21 * 2. * x21 - x20;
    x23 = x21 * 2. * x22 - x21;
    x24 = x21 * 2. * x23 - x22;
    x25 = x21 * 2. * x24 - x23;
    x26 = x21 * 2. * x25 - x24;
    x27 = x21 * 2. * x26 - x25;
    x28 = x21 * 2. * x27 - x26;
    x29 = x21 * 2. * x28 - x27;
    x210 = x21 * 2. * x29 - x28;
    x211 = x21 * 2. * x210 - x29;
    x212 = x21 * 2. * x211 - x210;

    return coeff[0] * x21 + coeff[1] + coeff[2] * x22 + coeff[3] * x23 +
            coeff[4] * x24 + coeff[5] * x25 + coeff[6] * x26 + coeff[7] * x27
            + coeff[8] * x28 + coeff[9] * x29 + coeff[10] * x11 + coeff[11] *
            x11 * x21 + coeff[12] * x210 + coeff[13] * x11 * x22 + coeff[14] *
             x211 + coeff[15] * x212 + coeff[16] * x11 * x25 + coeff[17] *
            x11 * x27 + coeff[18] * x11 * x26;
}

