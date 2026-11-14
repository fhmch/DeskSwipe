// ============================================================================
// DeskSwipe & ErgoSwipe — Parametric 3D Printable Desk Mods (OpenSCAD / MakerWorld Customizer)
// License: CC BY-NC-SA 4.0 | https://fhmch.github.io/DeskSwipe/
// ============================================================================

/* [Parameters] */
// Tabletop Thickness in mm (measure your desk before printing)
desk_thickness = 25.0; // [15:0.5:45]
// Clamp Width in mm
clamp_width = 24.0; // [15:1:40]
// Wall Thickness in mm (4.5mm+ recommended for PETG/PLA+)
wall_thickness = 4.5; // [3:0.5:8]
// Clamp Jaw Depth in mm
jaw_depth = 38.0; // [25:1:60]
// Part Type ("cable_clip", "headphone_hook")
part_type = "cable_clip"; // ["cable_clip", "headphone_hook"]

module cable_clip() {
    // Top Jaw
    translate([0, 0, wall_thickness + desk_thickness])
        cube([jaw_depth, clamp_width, wall_thickness]);
    // Spine
    translate([0, 0, wall_thickness])
        cube([wall_thickness, clamp_width, desk_thickness]);
    // Bottom Jaw
    cube([jaw_depth, clamp_width, wall_thickness]);
    // 3 Cable Slots
    for (fx = [6, 17, 28]) {
        translate([fx, 0, -10])
            cube([3.5, clamp_width, 10]);
        translate([fx, 0, -12.5])
            cube([5.5, clamp_width, 2.5]);
    }
}

module headphone_hook() {
    // Top Jaw
    translate([0, 0, wall_thickness + desk_thickness])
        cube([jaw_depth, clamp_width, wall_thickness]);
    // Spine + Hanger Drop
    translate([0, 0, -45])
        cube([wall_thickness, clamp_width, 45 + 2 * wall_thickness + desk_thickness]);
    // Bottom Jaw
    translate([wall_thickness, 0, 0])
        cube([jaw_depth * 0.85, clamp_width, wall_thickness]);
    // Headphone Cradle
    translate([-38, 0, -45])
        cube([38, clamp_width, wall_thickness]);
    // Retention Lip
    translate([-38, 0, -45 + wall_thickness])
        cube([wall_thickness, clamp_width, 17]);
}

if (part_type == "cable_clip") {
    cable_clip();
} else {
    headphone_hook();
}
