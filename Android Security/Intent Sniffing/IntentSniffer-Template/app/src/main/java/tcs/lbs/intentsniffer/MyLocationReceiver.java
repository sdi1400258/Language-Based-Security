package tcs.lbs.intentsniffer;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.widget.TextView;

public class MyLocationReceiver extends BroadcastReceiver {
    private TextView LatitudeTextView;
    private TextView LongitudeTextView;

    public MyLocationReceiver(TextView latitudeTextView, TextView longitudeTextView) {
        this.LatitudeTextView = latitudeTextView;
        this.LongitudeTextView = longitudeTextView;
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        Location location = intent.getParcelableExtra("Location");
        if (location != null) {
            LatitudeTextView.setText(String.valueOf(location.getLatitude()));
            LongitudeTextView.setText(String.valueOf(location.getLongitude()));
        }
    }
}