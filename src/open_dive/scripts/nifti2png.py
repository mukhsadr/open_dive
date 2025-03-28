import argparse
from pathlib import Path

from open_dive.viz import plot_nifti


def main():
    # Create args
    parser = argparse.ArgumentParser(description="Plot a slice of a NIFTI file")
    parser.add_argument("-n", "--nifti_path", type=Path, help="Path to NIFTI to plot")
    parser.add_argument(
        "-s", "--slice", default="m", help='Slice index (integer) or "m" for middle slice'
    )
    parser.add_argument(
        "-o",
        "--orientation",
        default="axial",
        help='Can be "axial", "sagittal" or "coronal"',
    )
    parser.add_argument(
        "--size", type=int, nargs=2, default=(600, 400), help="Size of window, by default (600,400)"
    )
    parser.add_argument("--save_path", help="Optional path to save to")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Whether to interactively show the scene",
    )
    parser.add_argument(
        "--value_range",
        type=int,
        nargs=2,
        help="Optional value range to pass to slicer. Default is min/max of image.",
    )
    parser.add_argument(
        "--volume_idx",
        type=int,
        help="Index of the volume to display if the image is 4D",
    )
    parser.add_argument(
        "--interpolation",
        default="nearest",
        help="Interpolation method to use (nearest or linear). Default is 'nearest'.",
    )
    parser.add_argument(
        "--scalar_colorbar",
        action="store_true",
        help="Whether to show a colorbar, by default True",
    )
    parser.add_argument(
        ## plot tractogram with slices
        "--tractography",
        type=Path,
        nargs="+",  # Accept one or more arguments
        help="Optional tractogram(s) to plot with slices. Can provide multiple files.",
    )
    parser.add_argument(
        "--tractography_values",
        type=float,
        nargs="+",
        help="Values to use for coloring each tractogram (must match number of tractography files)",
    )
    parser.add_argument(
        "--tractography_cmap",
        help="Matplotlib or cmcrameri colormap to use for tractography. Default is plasma if tractograph_values is provided, otherwise Set1.",
    )
    parser.add_argument(
        "--tractography_cmap_range",
        type=float,
        nargs=2,
        help="Optional range to use for the colormap. Default is 0 to 1.",
    )
    parser.add_argument(
        "--tractography_opacity",
        type=float,
        default=0.6,
        help="Optional value to use for the tractogram opacity in range (0, 1). Default is 0.6.",
    )
    parser.add_argument(
        "--tractography_colorbar",
        action="store_true",
        help="Whether to show a tractography values colorbar, by default False",
    )

    parser.add_argument("--tensor_image", type=Path, help="Path to tensor image, format is Dxx, Dxy, Dyy, Dxz, Dyz, Dzz. (Requires --nifti_path to be set).")
    parser.add_argument("--odf_image", type=Path, help="Path to orientation distribution function image represented as spherical harmonics. (Requires --nifti_path to be set).")
    parser.add_argument("--sh_basis", default="descoteaux07", help="Spherical harmonic basis, either 'descoteaux07' (default) or 'tournier07'")
    parser.add_argument("--scale", type=float, default=1, help="Scale of the tensor glyphs or ODF glyphs (default: 1)")
    parser.add_argument("--glass_brain", type=Path, help="Path to binary mask to generate glass brain from.")
    parser.add_argument("--azimuth", "--az", type=float, default=None, help="Azimuthal angle of the view (default: None)")
    parser.add_argument("--elevation", "--el", type=float, default=None, help="Elevation angle of the view (default: None)")

    args = parser.parse_args()

    # Plot the NIFTI
    plot_nifti(
        nifti_path=args.nifti_path,
        data_slice=args.slice,
        orientation=args.orientation,
        size=args.size,
        volume_idx=args.volume_idx,
        save_path=args.save_path,
        interactive=args.interactive,
        value_range=args.value_range,
        interpolation=args.interpolation,
        scalar_colorbar=args.scalar_colorbar,
        tractography=args.tractography,
        tractography_opacity=args.tractography_opacity,
        tractography_values=args.tractography_values,
        tractography_cmap=args.tractography_cmap,
        tractography_cmap_range=args.tractography_cmap_range,
        tractography_colorbar=args.tractography_colorbar,
        tensor_image=args.tensor_image,
        odf_image=args.odf_image,
        sh_basis=args.sh_basis,
        scale=args.scale,
        azimuth=args.azimuth,
        elevation=args.elevation,
        glass_brain_path=args.glass_brain,
    )

